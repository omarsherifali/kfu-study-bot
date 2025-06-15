import telebot
from telebot import types

BOT_TOKEN = '7689783688:AAEPJYMnkbzX_NPhymN6K2c6rHuaWtX_3dI'
bot = telebot.TeleBot(BOT_TOKEN)

# Drive links
anatomy_link = "https://drive.google.com/drive/folders/1f2Zp7gxWG6XR53JWBZV40YxndP-4ul5k"

# /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📘 Semester 1")
    btn2 = types.KeyboardButton("📗 Semester 2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "👋 Welcome to KFU Med Bot!\nChoose a semester:", reply_markup=markup)

# Handle Semester selection
@bot.message_handler(func=lambda message: message.text == "📘 Semester 1")
def sem1_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Anatomy – Sem 1", "Back to Main"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📘 Choose a subject from Semester 1:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📗 Semester 2")
def sem2_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Anatomy – Sem 2", "Back to Main"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📗 Choose a subject from Semester 2:", reply_markup=markup)

# Anatomy Sem 1
@bot.message_handler(func=lambda message: message.text == "Anatomy – Sem 1")
def sem1_anatomy(message):
    bot.send_message(message.chat.id, f"📘 Anatomy – Semester 1:\n{anatomy_link}")

# Anatomy Sem 2
@bot.message_handler(func=lambda message: message.text == "Anatomy – Sem 2")
def sem2_anatomy(message):
    bot.send_message(message.chat.id, f"📗 Anatomy – Semester 2:\n{anatomy_link}")

# Back to main menu
@bot.message_handler(func=lambda message: message.text == "Back to Main")
def back_to_main(message):
    start(message)

# Start polling
bot.polling()
