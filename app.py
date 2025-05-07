import os
from flask import Flask, request
from telegram import Bot
import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running with webhook!"

@app.route("/webhook", methods=["POST"])
def webhook():
    send_daily_poll()
    return "ok", 200

def send_daily_poll():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    question = f"What are your main tasks for today? ({today})"
    options = ["Client editing", "Studio shoot", "Location shoot", "Backups", "Retouching"]
    bot.send_poll(chat_id=CHAT_ID, question=question, options=options, is_anonymous=False)

if __name__ == "__main__":
    app.run()
