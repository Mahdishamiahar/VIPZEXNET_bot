from flask import Flask
from bot import bot
from threading import Thread

app = Flask(__name__)

@app.route('/')
def health():
    return "✅ ربات VIPZEXNET فعال است!"

@app.before_first_request
def activate_bot():
    Thread(target=bot.infinity_polling, daemon=True).start()

if __name__ == '__main__':
    app.run()