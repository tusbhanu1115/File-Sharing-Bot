import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

API_TOKEN = '5854990217:AAHljj4XJGdtUnp8fFdoEXBm9EviDNdH7WM'  # Replace with your actual API token
WEBHOOK_URL = 'https://drab-ruby-seal-hose.cyclic.app/'  # Replace with your webhook URL
WEBHOOK_PATH = '/webhook'  # Replace with your desired webhook path

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

class WebhookHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        update_data = self.rfile.read(content_length)
        update = telebot.types.Update.de_json(update_data.decode('utf-8'))
        bot.process_new_updates([update])
        self._set_response()

def run_server():
    server_address = ('', 3000)  # Update port number if needed
    httpd = HTTPServer(server_address, WebhookHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    run_server()
