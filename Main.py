import telebot
from telebot import types

BOT_TOKEN = '7689783688:AAEPJYMnkbzX_NPhymN6K2c6rHuaWtX_3dI'
bot = telebot.TeleBot(BOT_TOKEN)

# /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📘 Semester 1", "📗 Semester 2")
    bot.send_message(message.chat.id, "👋 Welcome to KFU Med Bot!\nChoose a semester:", reply_markup=markup)

# SEMESTER 1
@bot.message_handler(func=lambda message: message.text == "📘 Semester 1")
def sem1_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Anatomy – Sem 1",
        "Medical Physics – Sem 1",
        "Inorganic Chemistry – Sem 1",
        "Introductory Practice – Sem 1",
        "Biology – Sem 1",
        "Medical Informatics – Sem 1",
        "Foreign Language – Sem 1",
        "Latin – Sem 1",
        "🔙 Back to Main"
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📘 Semester 1 Subjects:", reply_markup=markup)

# SEMESTER 2
@bot.message_handler(func=lambda message: message.text == "📗 Semester 2")
def sem2_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Anatomy – Sem 2",
        "Organic Chemistry – Sem 2",
        "Foreign Language – Sem 2",
        "Latin – Sem 2",
        "Philosophy – Sem 2",
        "Medical Physics – Sem 2",
        "Biology (Parasitology) – Sem 2",
        "Histology – Sem 2",
        "Russian Language – Sem 2",
        "WRIS – Sem 2",
        "🔙 Back to Main"
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📗 Semester 2 Subjects:", reply_markup=markup)

# Placeholder replies for each subject
@bot.message_handler(func=lambda message: "– Sem" in message.text)
def subject_soon(message):
    bot.send_message(message.chat.id, f"{message.text}:\nComing soon 🔧")

# Back to main menu
@bot.message_handler(func=lambda message: message.text == "🔙 Back to Main")
def back_to_main(message):
    start(message)

# Keep the bot running
bot.polling()
