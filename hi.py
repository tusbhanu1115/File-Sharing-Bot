import telebot

API_TOKEN = '5854990217:AAHljj4XJGdtUnp8fFdoEXBm9EviDNdH7WM'  # Replace with your actual API token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.text.startswith('/start'):
        start_value = message.text.split('/start ')[1]
        bot.reply_to(message, f"Received start value: {start_value}")

@bot.message_handler(commands=['genlink'])
def handle_genlink(message):
    bot.reply_to(message, "Please send a file.")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_id = message.document.file_id
    bot.reply_to(message, f"Received file ID: {file_id}")

bot.polling()
