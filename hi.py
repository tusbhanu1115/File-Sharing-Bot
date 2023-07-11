import telebot

API_TOKEN = '5854990217:AAHljj4XJGdtUnp8fFdoEXBm9EviDNdH7WM'  # Replace with your actual API token
WEBHOOK_URL = 'https://drab-ruby-seal-hose.cyclic.app/'  # Replace with your webhook URL

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.text.startswith('/start'):
        split_text = message.text.split('/start ')
        if len(split_text) > 1:
            start_value = split_text[1]
            bot.reply_to(message, f"Received start value: {start_value}")
        else:
            bot.reply_to(message, "No start value found in the link.")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    # Start the bot's polling
    bot.polling()
