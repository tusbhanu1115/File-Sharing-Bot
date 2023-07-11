import telebot
from flask import Flask, request

API_TOKEN = '5854990217:AAHljj4XJGdtUnp8fFdoEXBm9EviDNdH7WM'  # Replace with your actual API token
WEBHOOK_URL = 'https://drab-ruby-seal-hose.cyclic.app/'  # Replace with your webhook URL
WEBHOOK_PATH = '/webhook'  # Replace with your desired webhook path

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

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

    # Run the Flask application
    app.run(host='0.0.0.0', port=3000)
