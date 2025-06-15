import telebot

# Replace with your actual BotFather token
BOT_TOKEN = '7689783688:AAEPJYMnkbzX_NPhymN6K2c6rHuaWtX_3dI'
bot = telebot.TeleBot(BOT_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to KFU Med Bot!\nType /anatomy to get anatomy lectures.")

# /anatomy command
@bot.message_handler(commands=['anatomy'])
def anatomy(message):
    bot.send_message(message.chat.id, "📚 Anatomy Lectures Folder:")
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1f2Zp7gxWG6XR53JWBZV40YxndP-4ul5k")

# keep the bot running
bot.polling()
