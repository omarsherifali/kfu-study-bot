import telebot
import os

API_TOKEN = '7689783688:AAEPJYMnkbzX_NPhymN6K2c6rHuaWtX_3dI'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to KFU Anatomy Bot! Type /help to see all commands.")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "/bones_upper\n/bones_lower\n/bones_skull\n/muscles_upper\n/muscles_lower\n/muscles_abdomen\n/muscles_intercostal")

def send_pdf(message, filename):
    path = os.path.join("files", filename)
    with open(path, "rb") as file:
        bot.send_document(message.chat.id, file)

@bot.message_handler(commands=['bones_upper'])
def handle_bones_upper(message):
    send_pdf(message, "bones_upper_1.pdf")

@bot.message_handler(commands=['bones_lower'])
def handle_bones_lower(message):
    send_pdf(message, "bones_lower_1.pdf")

@bot.message_handler(commands=['bones_skull'])
def handle_bones_skull(message):
    send_pdf(message, "bones_skull_1.pdf")

@bot.message_handler(commands=['muscles_upper'])
def handle_muscles_upper(message):
    send_pdf(message, "muscles_upper_1.pdf")

@bot.message_handler(commands=['muscles_lower'])
def handle_muscles_lower(message):
    send_pdf(message, "muscles_lower_1.pdf")

@bot.message_handler(commands=['muscles_abdomen'])
def handle_muscles_abdomen(message):
    send_pdf(message, "muscles_abdomen_1.pdf")

@bot.message_handler(commands=['muscles_intercostal'])
def handle_muscles_intercostal(message):
    send_pdf(message, "muscles_intercostal_1.pdf")

bot.infinity_polling()
