import telebot

bot = telebot.TeleBot('6648964856:AAEl3d48O2kL71dxEpFrK8CAgL2Oy9kLkoY')


from telebot import types

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Русский язык
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔍 Поиск")
        btn2 = types.KeyboardButton('💼 Аккаунт')
        btn3 = types.KeyboardButton('📃 Помощь')
        btn4 = types.KeyboardButton('🙍‍♂️ Информация')
        btn5 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "👋 Вас приветствует OSINT-бот от Saylent Team!", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '👀 Не забудь подписаться на официальный канал! @sectoraphobia':
        for i in range(10):
            bot.send_message(message.from_user.id, random.choice(spacefacts))

    elif message.text == '🔍 Поиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '👁️ Вы можете выполнить поиск следующим способом:\n\n📞 По номеру телефона: +79991231212\n📝По телеграм айди или юзернейму: @UserOsint, 1545524566\n\n🗣️ Используйте только проверенные сервисы по типу нашего, отличный OSINT инструмент\n\n⬇ Выберите подраздел', reply_markup=markup)

if message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔍 Поиск")
        btn2 = types.KeyboardButton('💼 Аккаунт')
        btn3 = types.KeyboardButton('📃 Помощь')
        btn4 = types.KeyboardButton('🙍‍♂️ Информация')
        btn5 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "👋 Вас приветствует OSINT-бот от Saylent Team!", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')


bot.polling(none_stop=True, interval=0)
