import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import checkpoints
import asyncio

check_points = checkpoints.get_points_data()
load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Хранилище для пользователя
user_data = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
default_comments = ["Точно!", "Ты ошибся, но ничего страшного"]


# start command - DONE
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton("Как это работает", callback_data='bot_info'))
    print("start_command")
    sent = await message.answer(
        "Привет, и с днем рождения!\n\
Пока границы закрыты, а поезда и самолеты до Турку не ходят, мы придумали, как всё же добраться до тебя в гости. Пусть и таким, немного волшебным, способом.\n\n\
Мы знаем, что ты наверняка уже изучила Турку вдоль и поперёк,  Поэтому мы не будем тебя учить, а просто предложим прогуляться по нашим следам. Интересно, удалось ли нам найти хоть один уголок, где ещё не ступала твоя нога?\n\n\
Считай, что этот квест — наш билет в Турку, а ты — наш проводник. Как если бы мы шли рядом, а ты показывала нам город и удивлялась вместе с нами: «О, а тут я никогда не была!»",
        reply_markup=keyboard
    )


#bot_info - DONE
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bot_'))
async def show_info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    print("show info function ----", user_data)
    user_data[user_id] = {'checkpoint_index': 0, 'step_index': 0}
    print(user_data)
    # Удаляем сообщение

    await bot.answer_callback_query(callback_query.id)

    info_text = "Выбирай любой удобный для себя день.\nНа прогулку понадобится 3-4 часа.\n\n\
А еще можно взять нас с собой онлайн по зуму.\n\n\
И отправляйся на старт"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("Адрес старта", callback_data='start_address')
    )

    await bot.send_message(user_id, info_text, reply_markup=keyboard)


#start_route - DONE
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
    if img_path:
        img_path = os.path.join(BASE_DIR, "img", cp[img + "_img_path"])
        await bot.send_photo(user_id, photo=open(img_path, 'rb'))


# DONE:Отправка истории - story_img_path + story_text
async def send_story(user_id, cp):
    if "story_text" in cp:
        if "story_img_path" in cp:
            await send_img("story", cp, user_id)
        await bot.send_message(user_id, cp["story_text"])
        await asyncio.sleep(10)


# DONE:Вопрос по истории или локации, local = "" / "local" - question + options + question_img_path
async def send_question(user_id, cp, index, local=""):
    q = "question"
    op = "options"
    if local:
        q = local + "_" + q
        op = local + "_" + op
    if q+"_intro" in cp:
        await bot.send_message(user_id, cp[q+"_intro"])
    if q in cp and op in cp:
        await asyncio.sleep(3)
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
        print(q, cp[q])
        try:
            await bot.send_message(user_id, cp[q])
            return False
        except Exception as e:
            print("error question without options", e)


# Кнопка "Я здесь" - DONE
async def send_here_btn(user_id, index):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Я здесь",
                                            callback_data=f"arrived_{index}"))

    await bot.send_message(user_id, "🔘", reply_markup=keyboard)


# DONE:кнопка "пошли дальше"
async def send_next_btn(user_id, index):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Пошли дальше", callback_data=f"next_{int(index) + 1}"))
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
            if step == "here_text":
                await asyncio.sleep(3)
            await send_message(step, user_id, cp)
        except Exception as e:
            print(e)

    # Кнопки
    elif step == "here_btn":
        await send_here_btn(user_id, index)
        return True
    elif step == "next_btn":
        try:
            await send_next_btn(user_id, lang)
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
    print("show", index, steps)
    # Идем по шагам до первой остановки (загадка, задание или кнопка)
    for i in range(len(steps)):
        step = steps[i]
        user_data[user_id]['step_index'] = i
        stop = await do_step(step, user_id, cp, index)
        if stop:
            break
    if not stop:
        await next_cp(user_id, index+1)


# DONE:Переход к следующему КП
async def next_cp(user_id, index):
    print("next", index, len(check_points), check_points)
    if index < len(check_points):
        user_data[user_id]['checkpoint_index'] = index
        user_data[user_id]['step_index'] = 0
        await show_checkpoint(user_id)
    else:
        await bot.send_message(user_id, "🎉 Квест завершён! Спасибо, что прошли его с нами!")


# DONE:Обработчик Я ЗДЕСЬ
@dp.callback_query_handler(lambda c: c.data.startswith("arrived_"))
async def arrived_handler(callback_query: types.CallbackQuery):
    _, index = callback_query.data.split("_")
    user_id = callback_query.from_user.id
    steps = checkpoints.get_steps_orden(int(index))
    cp = check_points[int(index)]

    # Удаляем кнопку
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    step_i = user_data[user_id]['step_index'] + 1
    print(step_i, len(steps))
    if step_i < len(steps):
        print("no")
        for i in range(step_i, len(steps)):
            step = steps[i]
            user_data[user_id]['step_index'] = i
            stop = await do_step(step, user_id, cp, index)
            if stop:
                break
    else:
        try:
            await next_cp(user_id, int(index)+1)
        except Exception as e:
            print(e)


# DONE:Обработчик ответов
@dp.callback_query_handler(lambda c: c.data.startswith("answer_"))
async def answer_handler(callback_query: types.CallbackQuery):
    _, index, selected, local = callback_query.data.split("_")
    index = int(index)
    user_id = callback_query.from_user.id
    cp = check_points[index]
    steps = checkpoints.get_steps_orden(int(index))

    #await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    selected = int(selected)
    ans = local + "_" + "answer" if local else "answer"
    ans_number = cp.get(ans)
    print(ans_number, ans)
    if ans_number:
        try:
            if selected == ans_number:
                await bot.send_message(user_id, default_comments[0])
            else:
                await bot.send_message(user_id, default_comments[1])
        except Exception as e:
            print("ans_number", e)
    else:
        ans_comments = ans + "_comments"
        comment = cp.get(ans_comments, {}).get(selected, {})
        print("comment", comment)
        if comment:
            try:
                await bot.send_message(user_id, comment)
            except Exception as e:
                print("comment", e)
    step_i = user_data[user_id]['step_index'] + 1
    print(step_i)
    await asyncio.sleep(3)
    if step_i < len(steps):
        for i in range(step_i, len(steps)):
            step = steps[i]
            user_data[user_id]['step_index'] = i
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
