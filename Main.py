import telebot

# Your real bot token here
BOT_TOKEN = '7689783688:AAEPJYMnkbzX_NPhymN6K2c6rHuaWtX_3dI'
bot = telebot.TeleBot(BOT_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to KFU Med Bot!\nUse the following commands:\n/sem1_anatomy\n/sem2_anatomy")

# Semester 1 - Anatomy
@bot.message_handler(commands=['sem1_anatomy'])
def sem1_anatomy(message):
    bot.send_message(message.chat.id, "📘 Semester 1 - Anatomy Lectures:")
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1f2Zp7gxWG6XR53JWBZV40YxndP-4ul5k")

# Semester 2 - Anatomy (same link for now)
@bot.message_handler(commands=['sem2_anatomy'])
def sem2_anatomy(message):
    bot.send_message(message.chat.id, "📘 Semester 2 - Anatomy Lectures:")
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1f2Zp7gxWG6XR53JWBZV40YxndP-4ul5k")

# Keep the bot running
bot.polling()
