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

checkpoints = {
    "1": [  # Маршрут 1
        {  # КП 0
            "title": {
                "ru": "Добро пожаловать в нашу историю!",
                "en": "Welcome to our story!",
                "es": "¡Bienvenidos a nuestra historia!"
            },
            "characters": ["Pablo&Poli"],
            "intro": {
                "ru": "Мы пройдем ее с вами шаг за шагом, рассказывая истории, и любуясь прекрасным городом.",
                "en": "We’ll walk through it with you step by step, sharing stories and admiring the beautiful city.",
                "es": "La recorreremos contigo paso a paso, contando historias y admirando esta hermosa ciudad."
            },
            "here_text": {
                "ru": "Вы стоите рядом с знаменитым памятником Петру Первому, основателю Санкт-Петербурга. \n\nС ним началась история этого города, отсюда начнется и наша история...",
                "en": "You are standing next to the famous monument of Peter the Great, the founder of Saint Petersburg.\n\nWith him, the story of this city began — and so will ours...",
                "es": "Estás junto al famoso monumento del Pedro el Grande, el fundador de San Petersburgo.\n\nCon él comenzó la historia de esta ciudad, y aquí comenzará la nuestra..."
            },
            "here_img_path": "HP0.jpg",
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
        {  # КП 2
            "title": {
                "ru": "КП 2: Инженер-конструктор",
                "en": "Checkpoint 2: ",
                "es": "Punto 2: "
            },
            "characters": ["Pablo_shi", "Pablo_muestra_mini", "Pablo&Poli_mira"],
            "intro": {
                "ru": "У меня тоже детство было занято экспериментами. Правда не физическими и химическими, а инженерными. \nСколько себя помню, папа всегда что-то строил, чинил, мастерил. С самого раннего детства я помогал ему возводить наш дом — стена за стеной. \n\nА мама учила меня готовить — терпеливо, с любовью. С тех пор во мне живут две страсти: создавать что-то своими руками и готовить что-то по-настоящему вкусное.",
                "en": "",
                "es": ""
            },
            "here_text": {
                "ru": "🏛️ Стоя у Адмиралтейства, прислушайся к каменным трубам: не кажется ли тебе, что эти сатиры трубят в честь маленьких, но важных побед?",
                "en": "",
                "es": ""
            },
            "here_img_path": "HP2-1.jpg",
            "question": {
                "ru": "🤔 Загадка\nЯ крутил педали, чтобы ехать вперёд… но когда хотел повернуть налево — приходилось делать вот что?",
                "en": "",
                "es": ""
            },
            "options": {
                "ru": ["Тянуть руль налево — как в обычной машине", "Крутить педали назад",
                       "Поворачивать колёса направо", "Вытянуть руку в окно и сигналить"],
                "en": [],
                "es": []
            },
            "answer_comments": {
                0: {
                    "ru": "Ха! Интуиция подвела. У моей машины были свои причуды! Руля у меня не было, так что чтобы повернуть налево, нужно было крутить задние колеса направо.",
                    "en": "",
                    "es": ""
                },
                1: {
                    "ru": "Ха! Интуиция подвела. У моей машины были свои причуды! Чтобы повернуть налево, нужно было крутить задние колеса направо",
                    "en": "",
                    "es": ""
                },
                2: {
                    "ru": "Ага! Руля у меня не было, так что чтобы повернуть налево, нужно было крутить задние колеса направо. Инженерная магия!",
                    "en": "",
                    "es": ""
                },
                3: {
                    "ru": "Ха! Интуиция подвела. У моей машины были свои причуды! Руля у меня не было, так что чтобы повернуть налево, нужно было крутить задние колеса направо.",
                    "en": "",
                    "es": ""
                }
            },
            "story_text": {
                "ru": (
                    "🎧 Гудок. Скрип тормозов. Весёлый гул детворы.\n"
                    "В одиннадцать лет я решил, что мне срочно нужна своя собственная машина. Не игрушка — настоящая.\n"
                    "Я нашёл где-то старые велосипедные колёса, пару железяк… и началось. Три дня я собирал её во дворе, как настоящий инженер-конструктор.\n"
                    "Никто не верил, что у меня получится, но всем было безумно интересно.\n"
                    "Каждый день ребятня сбегалась со всей округи, чтобы наблюдать, как продвигается мой проект.\n"
                    "И вот — всё готово.\n\n"
                    "Я лёг в самодельную кабину, как в болид Формулы-1, нажал на педали — и поехал!\n"
                    "Это был триумф."
                ),
                "en": (

                ),
                "es": (

                )
            },
            "audio_path": {
                "es": "",
            },
            "after_story_text": {
                "ru": (
                    "Один из дядей даже подарил мне мотор, чтобы следующая машина была уже с двигателем.\n"
                    "Мотор, правда, потерялся. "
                    "А вот радость от мечты, воплощённой своими руками, осталась со мной навсегда."
                ),
                "en": "",
                "es": ""
            },
            'local_question': {
                "ru": "🤔 Задание\n Кстати, рядом с Адмиралтейством, где мы стоим, стоит еще один инженер-конструктор - “Царь-плотник”.\nЧто Петр держит в руке?",
                "en": "",
                "es": ""
            },
            'local_options': {
                "ru": ["лопату", "топор",
                       "шпагу", "рубанок"],
                "en": [],
                "es": []
            },
            'local_answer': 1,
            'local_question_img_path': "LQP2-1.jpg"
        },
        {  # КП 2.5 Львы
            "title": {
                "ru": "Дополнительное КП. Символы",
                "en": "",
                "es": ""
            },
            "characters": ["Pablo&Poli_cositas", "Pablo_foto"],
            "intro": {
                "ru": "Символ Петербурга, конечно, лев. Они тут повсюду — на фасадах, мостах, лестницах. Мощные, грациозные.",
                "en": "",
                "es": ""
            },
            "here_text": {
                "ru": "Один из самых знаменитых символов находится здесь неподалеку, у подножия Дворцового моста.",
                "en": "",
                "es": ""
            },
            "here_img_path": "HP2-5-1.jpg",
            "question": {
                "ru": "🤔 Загадка\nВы наверное уже догадались, что символами нашей пары являются мишка и жирафик. \n\nА кто знает, какой головной убор первоначально был у жирафика?",
                "en": "",
                "es": ""
            },
            "options": {
                "ru": ["Дамская шляпка", "Колумбийское сомбереро",
                       "Красная шапочка"],
                "en": [],
                "es": []
            },
            "answer": 2,
            'local_question': {
                "ru": "🤔 Задание\n Сделайте групповое фото со львами - символами Петербурга и поделитесь с нами",
                "en": "",
                "es": ""
            },
        }
    ],
    "2": [  # Маршрут 2
        {  # КП 0
            "title": {
                "ru": "Добро пожаловать в нашу историю!",
                "en": "Welcome to our story!",
                "es": "¡Bienvenidos a nuestra historia!"
            },
            "characters": ["Pablo&Poli"],
            "intro": {
                "ru": "Мы пройдем ее с вами шаг за шагом, рассказывая истории, и любуясь прекрасным городом.",
                "en": "We’ll walk through it with you step by step, sharing stories and admiring the beautiful city.",
                "es": "La recorreremos contigo paso a paso, contando historias y admirando esta hermosa ciudad."
            },
            "here_text": {
                "ru": "Вы стоите рядом с знаменитым памятником Петру Первому, основателю Санкт-Петербурга. \n\nС ним началась история этого города, отсюда начнется и наша история...",
                "en": "You are standing next to the famous monument of Peter the Great, the founder of Saint Petersburg.\n\nWith him, the story of this city began — and so will ours...",
                "es": "Estás junto al famoso monumento del Pedro el Grande, el fundador de San Petersburgo.\n\nCon él comenzó la historia de esta ciudad, y aquí comenzará la nuestra..."
            },
            "here_img_path": "HP0.jpg",
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
                1: {
                    "ru": "Реактор я до восемнадцати лет не трогала, а вот бомбочки...",
                    "en": "I didn’t touch a reactor until I was eighteen, but the bombs…",
                    "es": "No toqué un reactor hasta los dieciocho, pero las bombitas…"
                },
                2: {
                    "ru": "Да вы меня хорошо знаете! Реактор я до восемнадцати лет не трогала, а вот бомбочки...",
                    "en": "You know me well! I didn’t touch a reactor until I was eighteen, but the bombs…",
                    "es": "¡Me conoces bien! No toqué un reactor hasta los dieciocho, pero las bombitas…"
                },
                3: {
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
        }
    ]
}

steps_orden = {
    "1": [  # Маршрут 1
        ["title", "character", "intro", "here_text", "here_img_path", "here_btn"],  # КП 0
        ["title", "character", "intro", "here_text", "here_img_path", "here_btn", "question",
         "story", "character", "after_story_text", "next_btn"],  # КП 1
        ["title", "character", "intro", "here_text", "here_img_path", "here_btn", "character", "story", "question",
         "after_story_text", "character", 'local_question', "next_btn"],  # КП 2
        ["title", "intro", "character", "here_text", "here_img_path", "here_btn", "question",
         "character", 'local_question', "next_btn"],  # КП 2.5 Львы
    ],
    "2": [
        ["title", "character", "intro", "here_text", "here_img_path", "here_btn"],  # КП 0
        ["title", "character", "intro", "here_text", "here_img_path", "here_btn", "question",
         "story", "character", "after_story_text", "next_btn"]  # КП 1
    ]  # Маршрут 2
}

character_ids = {
    "Pablo&Poli": "CAACAgIAAxkBAAIB6WhD-Lm42MDMSwPy24vTe6CzCOsyAAJTdAACYXsYSolgA5PFFEK8NgQ",
    "Poli": "CAACAgIAAxkBAAIB8mhD_1LJhh-6KU7w3vpYvqqVuDRsAAKVdgACxL4YSsMaPLkdqCipNgQ",
    "Pablo_ehehe": "CAACAgIAAxkBAAIB9GhD_3pw8uYO27iKIlioOlj9JSoYAAICagAC7vQZSvwKuoYH2pG9NgQ",
    "Poli_cafe": "CAACAgIAAxkBAAIB9mhD_4MCZD4AAe_NS0Ypx8nFy2ry-wACHoAAAk5uGUo1kM219vjssDYE",
    "Pablo_canta": "CAACAgIAAxkBAAIB-GhD_80iNEKtOnoSsRjWyDtPtOBSAALKbAACs-EhSlXJ_05m5CQ9NgQ",
    "Pablo_muestra": "CAACAgIAAxkBAAIB-mhD_9OXOtK5uMw0qDh-uY9vvZjXAAKSdgACzR8hSgT_tgpli2NnNgQ",
    "Poli_foto": "CAACAgIAAxkBAAIB_GhEAAH53IbaBRFQDT_Ntau8XzRhRgAC4XsAAiE8GEov12M-IkQgjDYE",
    "Pablo&Poli_viajadores": "CAACAgIAAxkBAAIB_mhEATQynT7D2oy6IOIrr3WzzTe0AAIScQACwb0gSj_96rlWmDUMNgQ",
    "Pablo_foto": "CAACAgIAAxkBAAICAAFoRAFpvKxsuGvoYgV_BLChETHfIQACZHYAAiPbGErCQLIPh4l3KzYE",
    "Pablo": "CAACAgIAAxkBAAICFGhEB09WuantNP12YFC8x6YoqKDGAALVbAACHt8hSsKonf5wIP_UNgQ",
    "Poli_exploradora": "CAACAgIAAxkBAAICCmhEAa8s6Y6MW7IxOnYCOVNcUxKjAAIfewAC1_MYSovCb1MaINXkNgQ",
    "Pablo_shi": "CAACAgIAAxkBAAICDmhEAbRKtjEzzkbXaUNCoaqO7PoEAALQbwACpmkhSrAElriqop9XNgQ",
    "Poli_asi": "CAACAgIAAxkBAAICDGhEAbJEd_tidRcgwwywo99nHRYjAAKbfgACF2IZSrGCNFOsvc3WNgQ",
    "Pablo_saxo": "CAACAgIAAxkBAAICCGhEAaxHuk875H0QTBMneTN90rA5AAIlcgACbRkZSlo1D5JfgwKSNgQ",
    "Pablo&Poli_amor": "CAACAgIAAxkBAAICBmhEAZA4JEQLHWJKOS2SbILIwg5gAAKQagACM7YgSrd_YyANu94KNgQ",
    "Pablo&Poli_camino": "CAACAgIAAxkBAAICBGhEAY3jHrU1NuktaPKwEArXEcuNAAJkbAAC4sogShxozmzc-3JoNgQ",
    "Pablo&Poli_mira": "CAACAgIAAxkBAAICAmhEAYiRKBQAAZeWA5gisanNZcGmgQACwW0AAr5aIEppO-mjcOx7ejYE",
    "Pablo&Poli_beso": "CAACAgIAAxkBAAICJGhEEIuso6sVlmfB2AABrXxY0pD2KQACrHYAAoqPIUrrD_UC1xT8ejYE",
    "Pablo&Poli_cositas": "CAACAgIAAxkBAAICImhEEIqc7_eFaf7DvWqF3b5hsV1pAAKkbgACY7chSjudeY9byPovNgQ",
    "Pablo_muestra_mini": "CAACAgIAAxkBAAICIGhEEInpeZ1znrvWQYJtKC25lBR-AAJVdgAClFkoShkl6AwdivJKNgQ",
    "Pablo_chef": "CAACAgIAAxkBAAICHmhEEIbIrR4KMOkJRe4LFMATRFBbAAJxbAACsmYgSlWsKyml2W9HNgQ",
    "Poli_nada": "CAACAgIAAxkBAAICHGhEEIXXC9JZH9luDrEKhqeoQahsAAIGcgACQd4gSpDaVkkTAAGJMTYE",
    "Poli_mona": "CAACAgIAAxkBAAICGmhEEIMyZnXqLrdbI3YuyIg-nmUzAAJRbgAC77kgSqR7KmrAqp-UNgQ",
    "Pablo_Poli": "CAACAgIAAxkBAAICGGhEEIGbIOnuxpPVvpibiD1UBWc7AAKiawACsuohSs0M7iF_E8ivNgQ",
    "Poli_Pablo": "CAACAgIAAxkBAAICFmhEEIBgZmHTLaev6E45yvNUQ449AAIzdgAC0REgSnTn4gLFPiSrNgQ",
    "Poli_hola": "CAACAgIAAxkBAAICJ2hEFT3jlGAAAfFdSDGMoChmopU7JQAC-XwAAoTQIErEX_6dQAwAAQ42BA"
}


def get_points_data():
    return checkpoints


def get_steps_orden(route, cp):
    return steps_orden[route][cp]


def get_sticker_id(name):
    return character_ids[name]
