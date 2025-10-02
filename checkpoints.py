"""
Структура checkpoints

'title' - Название КП - есть всегда
'characters' - Персонаж (Poli / Pablo) - есть всегда, назван по названию изображения из папки characters, список, берутся по очереди для одного КП
'intro' - Вводный текст, только если надо текст до кнопки "я здесь" разбить на 2 части
'here_text' - Текст перед кнопкой "я здесь", если есть intro, то отправляется с задержкой 5 сек - всегда
'here_img_path' - Название изображения из папки img, фото локации, находится непосредственно перед кнопкой "я здесь" - всегда
'question_intro' - Текст, если дополнительно нужно подвести к вопросу
'question' - Вопрос по нашей истории
'options' - Варианты ответа (лучше в видео опроса), не исчезают
'answer_comments' - Коментарии к выбранному ответу
'question_img_path' - Имя изображения к заданию, лежит в папке img
'story_text' - Текст нашей истории
'audio_path' - Имя аудио-версии текста, лежит в папке mp3
'story_img_path' - Имя иллюстрации к истории, лежит в папке img
'after_story_text' - Заключение после истории
'local_question_intro' - Текст, если дополнительно нужно подвести к вопросу по локации
'local_question' - Вопрос по локации
'local_options' - Варианты ответа к вопросу по локации, при выборе исчезают
'local_answer_comments' - Комментарии к выбранным ответам к заданию по локации
'local_answer' - номер правильного ответа, если стандартные ответы (угадал - нет)
'local_question_img_path' - Имя изображения к заданию по локации, лежит в папке img
'next_btn_text' - Текст непостредственно перед кнопкой "пошли дальше"
"""

checkpoints = [
        {  # КП 0
            "here_text": "Набережная реки Ауры, неподалеку от Морского музея (Linnankatu 72), Турку",
            "here_img_path": "CP0.jpg",
        },
        {  # КП 1
            "title": {
                "ru": "КП 1: Маленький экспериментатор",
                "en": "Checkpoint 1: Little scientist",
                "es": "Punto 1: La pequeña experimentadora"
            },
            "characters": ["Poli_hola", "Poli_Pablo"],
            "intro": {
                "ru": "В Петербурге зарождалась российская наука, первую академию наук учредил еще Петр I, ничего удивительного, что с детства меня окружали ученые.",
                "en": "Russian science was born in Saint Petersburg — Peter the Great founded the first Academy of Sciences. No wonder I was surrounded by scientists since childhood.",
                "es": "La ciencia rusa nació en San Petersburgo — Pedro el Grande fundó la primera Academia de Ciencias. No es de extrañar que desde niña estuviera rodeada de científicos."
            },
            "here_text": {
                "ru": "На другой стороне Невы расположились первые здания академии и университета, учрежденные еще в 1724 году",
                "en": "Across the Neva River stood the first buildings of the Academy and University, founded back in 1724.",
                "es": "Al otro lado del río Neva se encontraban los primeros edificios de la academia y la universidad, fundados en 1724."
            },
            "here_img_path": "HP1.jpg",
            "question_intro": {
                "ru": "Я росла в среде ученых, мой папа, дедушка и бабушка были физиками, поэтому наше с братом детство было наполнено захватывающими экспериментами 🧪",
                "en": "I grew up among scientists — my dad, grandpa, and grandma were all physicists, so my brother and I had a childhood full of thrilling experiments 🧪",
                "es": "Crecí entre científicos — mi padre, mi abuelo y mi abuela eran físicos, así que mi hermano y yo tuvimos una infancia llena de experimentos emocionantes 🧪"
            },
            "question": {
                "ru": "🤔 Загадка\nКак думаете, что умеет делать ребёнок в России к 10 годам?",
                "en": "🤔 Riddle\nWhat do you think a child in Russia can do by age of 10?",
                "es": "🤔 Acertijo\n¿Qué crees que puede hacer un niño en Rusia a los 10 años?"
            },
            "options": {
                "ru": ["Собрать карманный ядерный реактор", "Сделать йодовую бомбу", "Кататься на велосипеде"],
                "en": ["Build a pocket nuclear reactor", "Make an iodine bomb", "Ride a bicycle"],
                "es": ["Construir un reactor nuclear de bolsillo", "Hacer una bomba de yodo", "Montar en bicicleta"]
            },
            "answer_comments": {
                0: {
                    "ru": "Реактор я до восемнадцати лет не трогала, а вот бомбочки...",
                    "en": "I didn’t touch a reactor until I was eighteen, but the bombs…",
                    "es": "No toqué un reactor hasta los dieciocho, pero las bombitas…"
                },
                1: {
                    "ru": "Да вы меня хорошо знаете! Реактор я до восемнадцати лет не трогала, а вот бомбочки...",
                    "en": "You know me well! I didn’t touch a reactor until I was eighteen, but the bombs…",
                    "es": "¡Me conoces bien! No toqué un reactor hasta los dieciocho, pero las bombitas…"
                },
                2: {
                    "ru": "Обычный ребёнок умеет кататься на велосипеде, но я же не совсем обычная. Реактор я до восемнадцати лет не трогала, а вот бомбочки...",
                    "en": "An ordinary child can ride a bicycle, but I wasn’t exactly ordinary. I didn’t touch a reactor until I was eighteen, but the bombs…",
                    "es": "Un niño normal puede montar en bicicleta, pero yo no era precisamente normal. No toqué un reactor hasta los dieciocho, pero las bombitas…"
                }
            },
            "story_text": {
                "ru": (
                    "🎧 Слышится глухое эхо под аркой.\n"
                    "Сначала — щёлк, будто ножовка по металлу.\n"
                    "Потом — «бум-бах!» и приглушённый мамин крик: «На улицу!»\n\n"
                    "В детстве мой папа часто устраивал для меня и брата настоящие научные шоу прямо дома.\n"
                    "Мы варили творог, распиливали батарейки, спорили за ужином о термодинамике — и всё это было абсолютно нормально.\n\n"
                    "Но одной из самых ярких была история с йодовыми бомбочками.\n"
                    "Мы с братом и папой наделали целый поднос этих маленьких «зарядов», которые взрывались от лёгкого прикосновения.\n"
                    "Мама выгнала нас с ними на улицу — и как только мы вышли из подъезда, порыв ветра сдул все бомбочки... прямо обратно внутрь!\n\n"
                    "БАБАХ. Все стены подъезда стали фиолетовыми.\n\n"
                    "Нам тогда было весело. Маме — не очень.\n"
                    "Но именно с таких сумасшедших экспериментов и началась моя любовь к науке."
                ),
                "en": (
                    "🎧 A hollow echo is heard under the arch.\n"
                    "First — a click, like a hacksaw on metal.\n"
                    "Then — ‘boom-bang!’ and a muffled mom’s scream: ‘Get outside!’\n\n"
                    "As a child, my dad often put on real science shows for me and my brother, right at home.\n"
                    "We made cottage cheese, sawed open batteries, discussed thermodynamics over dinner — and all of it was completely normal.\n\n"
                    "But one of the brightest memories was the iodine bombs.\n"
                    "My brother, dad, and I made a whole tray of those tiny ‘charges’ that exploded with the slightest touch.\n"
                    "Mom kicked us out with them — and just as we stepped outside, a gust of wind blew all the bombs… right back inside!\n\n"
                    "BOOM. All the walls in the stairwell turned purple.\n\n"
                    "We thought it was fun. Mom — not so much.\n"
                    "But that’s how my love for science began — through wild experiments like these."
                ),
                "es": (
                    "🎧 Se oye un eco sordo bajo el arco.\n"
                    "Primero — un clic, como una sierra en metal.\n"
                    "Luego — ¡boom-bang! y el grito apagado de mamá: «¡A la calle!»\n\n"
                    "De niña, mi papá solía hacer verdaderos espectáculos científicos para mí y mi hermano, en casa.\n"
                    "Hacíamos queso fresco, abríamos pilas con una sierra, discutíamos sobre termodinámica durante la cena — y todo eso nos parecía totalmente normal.\n\n"
                    "Pero uno de los recuerdos más vívidos fue el de las bombas de yodo.\n"
                    "Mi papá, mi hermano y yo hicimos una bandeja entera de esas pequeñas ‘cargas’ que explotaban con el más leve toque.\n"
                    "Mamá nos echó con ellas — y justo al salir, una ráfaga de viento las devolvió… ¡directo al interior!\n\n"
                    "¡BOOM! Todas las paredes de la entrada quedaron moradas.\n\n"
                    "Para nosotros fue divertido. Para mamá — no tanto.\n"
                    "Pero fue con esos locos experimentos como nació mi amor por la ciencia."
                )
            },
            "audio_path": {
                "ru": "КП 1.mp3",
            },
            "story_img_path": "SP1.jpg",
            "after_story_text": {
                "ru": "Мне уже не терпится узнать, какое же детство было у Пабло, а вам?",
                "en": "I can’t wait to hear what childhood Pablo had — and you?",
                "es": "Ya estoy curiosa por saber qué infancia tuvo Pablo, ¿y tú?"
            }
        },
]

steps_orden = [  # Маршрут 1
        ["here_text", "here_img_path", "here_btn"],  # КП 0
    ]



def get_points_data():
    return checkpoints


def get_steps_orden(cp):
    return steps_orden[cp]


