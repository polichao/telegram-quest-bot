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

# Хранилище для пользователя: язык и маршрут
user_data = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
default_comments = {
    "ru": ["Точно!", "Ты ошибся, но ничего страшного"],
    "en": ["Yes!", "Sorry, but you didn't guess"],
    "es": ["Exacto!", "Lo siento, está vez no adivinaste"]
}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        types.InlineKeyboardButton("Русский 🇷🇺", callback_data='lang_ru'),
        types.InlineKeyboardButton("English 🇬🇧", callback_data='lang_en'),
        types.InlineKeyboardButton("Español 🇪🇸", callback_data='lang_es')
    )
    sent = await message.answer(
        "Привет! Пожалуйста, выберите язык / Please choose your language / Por favor, elige tu idioma:",
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lang_'))
async def language_chosen(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    lang = callback_query.data.split('_')[1]

    user_data[user_id] = {'lang': lang}
    user_data[user_id]['checkpoint_index'] = 0
    user_data[user_id]['step_index'] = 0
    user_data[user_id]['character_index'] = -1

    # Удаляем сообщение с кнопками выбора языка
    try:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    except Exception as e:
        print(f"Не удалось удалить сообщение: {e}")

    await bot.answer_callback_query(callback_query.id)

    greetings = {
        'ru': "Вы выбрали русский язык. Приветствуем на нашем свадебном квесте!\nВыберите маршрут:",
        'en': "You chose English. Welcome to our wedding quest!\nPlease choose your route:",
        'es': "Has elegido español. ¡Bienvenido a nuestra búsqueda de boda!\nPor favor, elige tu ruta:"
    }
    routes_buttons = {
        'ru': ["Маршрут 1", "Маршрут 2"],
        'en': ["Route 1", "Route 2"],
        'es': ["Ruta 1", "Ruta 2"]
    }

    labels = routes_buttons.get(lang, routes_buttons['en'])
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(labels[0], callback_data='route_1'),
        types.InlineKeyboardButton(labels[1], callback_data='route_2')
    )

    await bot.send_message(user_id, greetings.get(lang, "Hello!\nChoose your route:"), reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('route_'))
async def route_chosen(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    route = callback_query.data.split('_')[1]

    # Добавляем маршрут к данным пользователя
    if user_id in user_data:
        user_data[user_id]['route'] = route
    else:
        user_data[user_id] = {'route': route}

    # Удаляем сообщение с выбором маршрута
    try:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    except Exception as e:
        print(f"Не удалось удалить сообщение: {e}")

    await bot.answer_callback_query(callback_query.id)

    messages = {
        'ru': f"Отлично! Вы выбрали маршрут {route}. Начнем!",
        'en': f"Great! You chose route {route}. Let's go!",
        'es': f"¡Genial! Has elegido la ruta {route}. ¡Empezamos!"
    }

    lang = user_data.get(user_id, {}).get('lang', 'en')
    await bot.send_message(user_id, messages.get(lang, messages['en']))
    await show_checkpoint(user_id)


# Функции обработки всех возможных шагов
# Отправка любого текста - title, intro, here_text, after_story_text,  next_btn_text
async def send_message(step, user_id, lang, cp):
    if step in cp:
        await bot.send_message(user_id, cp[step][lang])


# Отправка любой фотографии из папки img - story_img_path, question_img_path, here_img_path, local_question_img_path
async def send_img(img, cp, user_id):
    img_path = cp.get(img + "_img_path")
    if img_path:
        img_path = os.path.join(BASE_DIR, "img", cp[img + "_img_path"])
        await bot.send_photo(user_id, photo=open(img_path, 'rb'))


# Отправка стикера с персонажем - по списку
async def send_character(cp, user_id):
    characters = cp.get("characters")
    user_data[user_id]["character_index"] += 1
    i = user_data[user_id]["character_index"]
    print("character", characters[i])
    if characters and -1 < i < len(characters):
        print(characters[i])
        sticker_id = checkpoints.get_sticker_id(characters[i])
        try:
            await bot.send_sticker(chat_id=user_id, sticker=sticker_id)
        except Exception as e:
            print(f"[Ошибка] Не удалось отправить стикер {sticker_id}: {e}")


# Отправка истории - audio_path + story_img_path + story_text
async def send_story(user_id, lang, cp, route, index):
    if "story_text" in cp:
        if "audio_path" in cp and cp["audio_path"].get(lang):
            audio_path = os.path.join(BASE_DIR, "mp3", cp["audio_path"][lang])
            await bot.send_audio(user_id, audio=open(audio_path, 'rb'))
            await send_img("story", cp, user_id)
            await asyncio.sleep(5)
        elif "story_img_path" in cp:
            await send_img("story", cp, user_id)
        await bot.send_message(user_id, cp["story_text"][lang])
        await asyncio.sleep(10)


# Вопрос по истории или локации, local = "" / "local" - question + options + question_img_path
async def send_question(user_id, lang, route, cp, index, local=""):
    q = "question"
    op = "options"
    if local:
        q = local + "_" + q
        op = local + "_" + op
    if q+"_intro" in cp:
        await bot.send_message(user_id, cp[q+"_intro"][lang])
    if q in cp and op in cp:
        await asyncio.sleep(3)
        keyboard = types.InlineKeyboardMarkup()

        for i, option in enumerate(cp[op][lang]):
            try:
                keyboard.add(types.InlineKeyboardButton(option, callback_data=f"answer_{route}_{index}_{i}_{local}"))
            except Exception as e:
                print("Не удалось добавить кнопку", e)
        try:
            await send_img(q, cp, user_id)
            await bot.send_message(user_id, cp[q][lang], reply_markup=keyboard)
            return True
        except Exception as e:
            print("Не удалось отправить кнопки", e)
    elif q in cp:
        print(q, cp[q][lang])
        try:
            await bot.send_message(user_id, cp[q][lang])
            return False
        except Exception as e:
            print("error question without options", e)


# Кнопка "Я здесь"
async def send_here_btn(user_id, lang, route, index):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton({
                                                'ru': "Я здесь",
                                                'en': "I'm here",
                                                'es': "Aquí estoy"
                                            }[lang], callback_data=f"arrived_{route}_{index}"))

    await bot.send_message(user_id, "🔘", reply_markup=keyboard)


# кнопка "пошли дальше"
async def send_next_btn(user_id, lang, route, index):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton({
        'ru': "Пошли дальше",
        'en': "Let's go",
        'es': "Sigamos"
    }[lang], callback_data=f"next_{route}_{int(index) + 1}"))
    await bot.send_message(user_id, "👉", reply_markup=kb)


# Обработка последовательности шагов
async def do_step(step, user_id, lang, route, cp, index):
    # Задания и история
    if step == "question":
        q = await send_question(user_id, lang, route, cp, index)
        return q
    elif step == "local_question":
        try:
            q = await send_question(user_id, lang, route, cp, index, "local")
            return q
        except Exception as e:
            print("do_step, local question", e)
    elif step == "story":
        await send_story(user_id, lang, cp, route, index)

    # Отправка любого текста - title, intro, here_text, after_story_text, question_intro, next_btn_text
    elif step in ['title', 'intro', 'here_text', 'after_story_text', 'next_btn_text']:
        try:
            if step == "here_text":
                await asyncio.sleep(3)
            await send_message(step, user_id, lang, cp)
        except Exception as e:
            print(e)

    # Кнопки
    elif step == "here_btn":
        await send_here_btn(user_id, lang, route, index)
        return True
    elif step == "next_btn":
        try:
            await send_next_btn(user_id, lang, route, index)
            return True
        except Exception as e:
            print(e)

    # отправка изображений и стикеров
    elif step == "here_img_path":
        try:
            await send_img("here", cp, user_id)
        except Exception as e:
            print("here img", e)
    elif step == "character":
        await send_character(cp, user_id)
    return False


# Функция выбора кп
async def show_checkpoint(user_id):
    user = user_data[user_id]
    route = user['route']
    lang = user['lang']
    index = user.get('checkpoint_index', 0)
    steps = checkpoints.get_steps_orden(route, int(index))
    cp = check_points[route][index]
    stop = False
    print("show", index, steps)
    # Идем по шагам до первой остановки (загадка, задание или кнопка)
    for i in range(len(steps)):
        step = steps[i]
        user_data[user_id]['step_index'] = i
        stop = await do_step(step, user_id, lang, route, cp, index)
        if stop:
            break
    if not stop:
        await next_cp(user_id, lang, route, index+1)


# Переход к следующему КП
async def next_cp(user_id, lang, route, index):
    print("next", index)
    if index < len(check_points[route]):
        user_data[user_id]['checkpoint_index'] = index
        user_data[user_id]['character_index'] = -1
        user_data[user_id]['step_index'] = 0
        await show_checkpoint(user_id)
    else:
        await bot.send_message(user_id, {
            'ru': "🎉 Квест завершён! Спасибо, что прошли его с нами!",
            'en': "🎉 Quest complete! Thank you for joining us!",
            'es': "🎉 ¡Búsqueda completada! ¡Gracias por participar!"
        }[lang])


# Обработчик Я ЗДЕСЬ
@dp.callback_query_handler(lambda c: c.data.startswith("arrived_"))
async def arrived_handler(callback_query: types.CallbackQuery):
    _, route, index = callback_query.data.split("_")
    user_id = callback_query.from_user.id
    lang = user_data[user_id]['lang']
    steps = checkpoints.get_steps_orden(route, int(index))
    cp = check_points[route][int(index)]

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
            stop = await do_step(step, user_id, lang, route, cp, index)
            if stop:
                break
    else:
        try:
            await next_cp(user_id, lang, route, int(index)+1)
        except Exception as e:
            print(e)


# Обработчик ответов
@dp.callback_query_handler(lambda c: c.data.startswith("answer_"))
async def answer_handler(callback_query: types.CallbackQuery):
    _, route, index, selected, local = callback_query.data.split("_")
    index = int(index)
    user_id = callback_query.from_user.id
    lang = user_data[user_id]['lang']
    cp = check_points[route][index]
    steps = checkpoints.get_steps_orden(route, int(index))

    #await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    selected = int(selected)
    ans = local + "_" + "answer" if local else "answer"
    ans_number = cp.get(ans)
    print(ans_number, ans)
    if ans_number:
        try:
            if selected == ans_number:
                await bot.send_message(user_id, default_comments[lang][0])
            else:
                await bot.send_message(user_id, default_comments[lang][1])
        except Exception as e:
            print("ans_number", e)
    else:
        ans_comments = ans + "_comments"
        comment = cp.get(ans_comments, {}).get(selected, {}).get(lang)
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
            stop = await do_step(step, user_id, lang, route, cp, index)
            if stop:
                break
    else:
        await next_cp(user_id, lang, route, int(index) + 1)


# Переход к следующему КП
@dp.callback_query_handler(lambda c: c.data.startswith("next_"))
async def next_checkpoint(callback_query: types.CallbackQuery):
    _, route, index = callback_query.data.split("_")
    index = int(index)
    user_id = callback_query.from_user.id
    lang = user_data[user_id]['lang']

    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)

    await next_cp(user_id, lang, route, index)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
