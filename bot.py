import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import checkpoints
import asyncio
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "data", "user_states.json")


def load_user_states():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {int(k): v for k, v in data.items()}
    return {}


def save_user_states(user_data):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=2)
    print(f"Saved user states for {len(user_data)} users")


# Загружаем сохраненные состояния
user_data = load_user_states()
print(f"Loaded user states for {len(user_data)} users")

check_points = checkpoints.get_points_data()
load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

default_comments = ["Точно!", "Ты ошибся, но ничего страшного"]


# start command - DONE
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton("Как это работает", callback_data='bot_info'))
    sent = await message.answer(
        "Привет, и с днем рождения!\n\
Пока границы закрыты, а поезда и самолеты до Турку не ходят, мы придумали, как всё же добраться до тебя в гости. Пусть и таким, немного волшебным, способом.\n\n\
Мы знаем, что ты наверняка уже изучила Турку вдоль и поперёк,  Поэтому мы не будем тебя учить, а просто предложим прогуляться по нашим следам. Интересно, удалось ли нам найти хоть один уголок, где ещё не ступала твоя нога?\n\n\
Считай, что этот квест — наш билет в Турку, а ты — наш проводник. Как если бы мы шли рядом, а ты показывала нам город и удивлялась вместе с нами: «О, а тут я никогда не была!»",
        reply_markup=keyboard
    )


# bot_info - DONE
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bot_'))
async def show_info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_data[user_id] = {'checkpoint_index': 0, 'step_index': 0}
    save_user_states(user_data)
    # Удаляем сообщение
    await bot.answer_callback_query(callback_query.id)

    info_text = "Выбирай любой удобный для себя день.\nНа прогулку понадобится 3-4 часа.\n\n\
А еще можно взять нас с собой онлайн по зуму.\n\n\
И отправляйся на старт"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("А где старт", callback_data='start_address')
    )

    await bot.send_message(user_id, info_text, reply_markup=keyboard)


# start_route - DONE
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('start_address'))
async def start_route(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Удаляем сообщение

    await bot.answer_callback_query(callback_query.id)

    await show_checkpoint(user_id)


# Функции обработки всех возможных шагов - DONE
# Отправка любого текста - title, intro, here_text, after_story_text,  next_btn_text
async def send_message(step, user_id, cp):
    if step in cp:
        await bot.send_message(user_id, cp[step])


# DONE:Отправка любой фотографии из папки img - story_img_path, question_img_path, here_img_path, local_question_img_path
async def send_img(img, cp, user_id):
    img_path = cp.get(img + "_img_path")
    #print("send-img", img_path)
    if img_path:
        img_path = os.path.join(BASE_DIR, "img", cp[img + "_img_path"])
        await bot.send_photo(user_id, photo=open(img_path, 'rb'))


# DONE:Отправка истории - story_img_path + story_text
async def send_story(user_id, cp, name=""):
    if name+"story_text" in cp:
        if name+"story_img_path" in cp:
            await send_img(name+"story", cp, user_id)
        await bot.send_message(user_id, cp[name+"story_text"])


# DONE:Вопрос по истории или локации, local = "" / "local" - question + options + question_img_path
async def send_question(user_id, cp, index, local=""):
    q = "question"
    op = "options"
    if local:
        q = local + "_" + q
        op = local + "_" + op
    if q + "_intro" in cp:
        await bot.send_message(user_id, cp[q + "_intro"])
    if q in cp and op in cp:
        keyboard = types.InlineKeyboardMarkup()

        for i, option in enumerate(cp[op]):
            try:
                keyboard.add(types.InlineKeyboardButton(option, callback_data=f"answer_{index}_{i}_{local}"))
            except Exception as e:
                print("Не удалось добавить кнопку", e)
        try:
            await send_img(q, cp, user_id)
            await bot.send_message(user_id, cp[q], reply_markup=keyboard)
            return True
        except Exception as e:
            print("Не удалось отправить кнопки", e)
    elif q in cp:
        #print(q, cp[q])
        try:
            await send_img(q, cp, user_id)
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                types.InlineKeyboardButton("Я здесь", callback_data=f'riddle_here_{index}_{local}'),
                types.InlineKeyboardButton("Хочу подсказку", callback_data=f'riddle_tip_{index}_{local}'),
            )
            await bot.send_message(user_id, cp[q], reply_markup=keyboard)
            return True
        except Exception as e:
            print("error question without options", e)


# Кнопка "Я здесь" - DONE
async def send_here_btn(user_id, index):
    text = "Я здесь"
    cp = check_points[int(index)]
    if "here_btn_text" in cp:
        text = cp["here_btn_text"]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text,
                                            callback_data=f"arrived_{index}"))

    await bot.send_message(user_id, "👍🏻", reply_markup=keyboard)


# DONE:кнопка "пошли дальше"
async def send_next_btn(user_id, index):
    text = "Пошли дальше"
    cp = check_points[int(index)]
    if "next_btn_text" in cp:
        text = cp["next_btn_text"]
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text, callback_data=f"next_{int(index) + 1}"))
    await bot.send_message(user_id, "👉", reply_markup=kb)


# DONE:Обработка последовательности шагов
async def do_step(step, user_id, cp, index):
    # Задания и история
    if step == "question":
        q = await send_question(user_id, cp, index)
        return q
    elif step == "local_question":
        try:
            q = await send_question(user_id, cp, index, "local")
            return q
        except Exception as e:
            print("do_step, local question", e)
    elif step == "story":
        await send_story(user_id, cp)

    # Отправка любого текста - title, intro, here_text, after_story_text, question_intro, next_btn_text
    elif step in ['title', 'intro', 'here_text', 'after_story_text', 'next_btn_text']:
        try:
            await send_message(step, user_id, cp)
        except Exception as e:
            print(e)

    # Кнопки
    elif step == "here_btn":
        await send_here_btn(user_id, index)
        return True
    elif step == "next_btn":
        try:
            await send_next_btn(user_id, index)
            return True
        except Exception as e:
            print(e)

    # отправка изображений и стикеров
    elif step == "here_img_path":
        try:
            await send_img("here", cp, user_id)
        except Exception as e:
            print("here img", e)
    return False


# DONE:Функция выбора кп
async def show_checkpoint(user_id):
    user = user_data[user_id]
    index = user.get('checkpoint_index', 0)
    steps = checkpoints.get_steps_orden(int(index))
    cp = check_points[index]
    stop = False
    #print("show", index, steps, cp)
    # Идем по шагам до первой остановки (загадка, задание или кнопка)
    for i in range(len(steps)):
        step = steps[i]
        user_data[user_id]['step_index'] = i
        save_user_states(user_data)  # СОХРАНЯЕМ после изменения шага!
        stop = await do_step(step, user_id, cp, index)
        print(step,i,index,stop)
        if stop:
            break
    if not stop:
        await next_cp(user_id, index + 1)


# DONE:Переход к следующему КП
async def next_cp(user_id, index):
    #print("next", index, len(check_points))
    if index < len(check_points):
        user_data[user_id]['checkpoint_index'] = index
        user_data[user_id]['step_index'] = 0
        save_user_states(user_data)  # СОХРАНЯЕМ!
        await show_checkpoint(user_id)
    else:
        await bot.send_message(user_id, "🎉 Квест завершён! Спасибо, что прошла его с нами! Приятного чаепития!")


# DONE:Обработчик Я ЗДЕСЬ
@dp.callback_query_handler(lambda c: c.data.startswith("arrived_"))
async def arrived_handler(callback_query: types.CallbackQuery):
    _, index = callback_query.data.split("_")
    user_id = callback_query.from_user.id
    steps = checkpoints.get_steps_orden(int(index))
    cp = check_points[int(index)]
    #print("ind", index)
    #print("cp", check_points[0])
    # Удаляем кнопку
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    step_i = user_data[user_id]['step_index'] + 1
    #print(step_i, len(steps))
    if step_i < len(steps):
        #print("no", cp)
        for i in range(step_i, len(steps)):
            step = steps[i]
            user_data[user_id]['step_index'] = i
            save_user_states(user_data)  # СОХРАНЯЕМ!
            stop = await do_step(step, user_id, cp, index)
            print(stop, step)
            if stop:
                break
    else:
        try:
            await next_cp(user_id, int(index) + 1)
        except Exception as e:
            print(e)


# Обработчик шага загадки "я здесь"
@dp.callback_query_handler(lambda c: c.data.startswith("riddle_here"))
async def riddle_here_handler(callback_query: types.CallbackQuery):
    #print(callback_query.data)
    _, _, index, local = callback_query.data.split("_")
    user_id = callback_query.from_user.id

    # Удаляем кнопку
    #await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    # Редактируем сообщение, убирая кнопки
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None  # убираем клавиатуру
    )
    await bot.answer_callback_query(callback_query.id)

    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("Показать разгадку", callback_data=f'riddle_answer_{index}_{local}'),
            types.InlineKeyboardButton("Пошли дальше", callback_data=f"arrived_{index}"),
        )
        await bot.send_message(user_id, "Выбери действие:", reply_markup=keyboard)
        return True
    except Exception as e:
        print("error question without options", e)


# Обработчик шага загадки "покажи разгадку]"
@dp.callback_query_handler(lambda c: c.data.startswith("riddle_answer"))
async def riddle_show_answer_handler(callback_query: types.CallbackQuery):
    #print(callback_query.data)
    _, _, index, local = callback_query.data.split("_")
    user_id = callback_query.from_user.id
    cp = check_points[int(index)]

    # Удаляем кнопку
    # await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    # Редактируем сообщение, убирая кнопки
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None  # убираем клавиатуру
    )
    await bot.answer_callback_query(callback_query.id)

    try:
        await send_story(user_id, cp, name="question_")
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton("👍🏻", callback_data=f"arrived_{index}"),
        )
        await bot.send_message(user_id, "Отлично! Я здесь.", reply_markup=keyboard)
        return True
    except Exception as e:
        print("error question without options", e)


# Обработчик шага загадки "подсказка"
@dp.callback_query_handler(lambda c: c.data.startswith("riddle_tip"))
async def riddle_show_tip_handler(callback_query: types.CallbackQuery):
    _, _, index, local = callback_query.data.split("_")
    user_id = callback_query.from_user.id
    cp = check_points[int(index)]

    # Удаляем кнопку
    # await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    # Редактируем сообщение, убирая кнопки
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None  # убираем клавиатуру
    )
    await bot.answer_callback_query(callback_query.id)

    try:
        info = ""
        local_ = local + "_" if local else ""
        if local_ + "question_tip" in cp:
            info = cp[local_ + "question_tip"]

        print("info---", info)
        if info or local_ + "question_tip_img_path" in cp:
            print("true")
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                types.InlineKeyboardButton("Я здесь.", callback_data=f'riddle_here_{index}_{local}'),
                types.InlineKeyboardButton("Сложно, помогите.", callback_data=f'riddle_answer_{index}_{local}')
            )
            if local_ + "question_tip_img_path" in cp:
                await send_img(local_+"question_tip", cp, user_id)
                info = "Присмотрись к картинке" if not info else info
        else:
            print("false")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(
                types.InlineKeyboardButton("Сложно, помогите.", callback_data=f'riddle_answer_{index}_{local}')
            )
            if not info:
                info = "Мы не придумали подсказку"
        await bot.send_message(user_id, info, reply_markup=keyboard)
        return True
    except Exception as e:
        print("error question without options", e)


# DONE:Обработчик ответов
@dp.callback_query_handler(lambda c: c.data.startswith("answer_"))
async def answer_handler(callback_query: types.CallbackQuery):
    _, index, selected, local = callback_query.data.split("_")
    index = int(index)
    user_id = callback_query.from_user.id
    cp = check_points[index]
    steps = checkpoints.get_steps_orden(int(index))

    # await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    selected = int(selected)
    ans = local + "_" + "answer" if local else "answer"
    ans_number = cp.get(ans)
    #print(ans_number, ans)
    comments = cp[ans+"_comments"] if ans+"_comments" in cp else default_comments
    comments_chars = cp[ans+"_comments_characters"] if ans+"_comments_characters" in cp else [None, None]
    if ans_number is not None:
        try:
            #print(comments_chars)
            if selected == ans_number:
                if comments_chars[0]:
                    img_path = os.path.join(BASE_DIR, "img", comments_chars[0])
                    await bot.send_photo(user_id, photo=open(img_path, 'rb'))
                await bot.send_message(user_id, comments[0])
            else:
                if comments_chars[1]:
                    img_path = os.path.join(BASE_DIR, "img", comments_chars[1])
                    await bot.send_photo(user_id, photo=open(img_path, 'rb'))
                await bot.send_message(user_id, comments[1])
        except Exception as e:
            print("ans_number", e)
    else:
        ans_comments = ans + "_comments"
        comment = cp.get(ans_comments, {})[selected]
        #print("comment", comment)
        if comment:
            try:
                await bot.send_message(user_id, comment)
            except Exception as e:
                print("comment", e)
    step_i = user_data[user_id]['step_index'] + 1
    #print(step_i)
    if step_i < len(steps):
        for i in range(step_i, len(steps)):
            step = steps[i]
            user_data[user_id]['step_index'] = i
            save_user_states(user_data)  # СОХРАНЯЕМ!
            stop = await do_step(step, user_id, cp, index)
            if stop:
                break
    else:
        await next_cp(user_id, int(index) + 1)


# DONE:Переход к следующему КП
@dp.callback_query_handler(lambda c: c.data.startswith("next_"))
async def next_checkpoint(callback_query: types.CallbackQuery):
    _, index = callback_query.data.split("_")
    index = int(index)
    user_id = callback_query.from_user.id

    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)

    await next_cp(user_id, index)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
