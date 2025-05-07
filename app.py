from flask import Flask, request
from telegram import Bot
import os
import datetime

# Correct way to get from environment variables
TOKEN = os.getenv("7599034036:AAHoltCH4gvuUxnxItsi-gL6yQ8FvfQ6GYM")
CHAT_ID = os.getenv("6393012286")

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
    options = [
        "1- أذكار الصباح",
        "2- التسبيح",
        "3- الإستغفار",
        "4- الصلاة على النبي",
        "5- لا اله الا الله والله اكبر",
        "6- لا اله الا الله وحده",
        "7- لا اله الا الله ولا شريك له",
        "8- لا اله الا الله ولا حول ولا قوة الا بالله",
        "9- أذكار المساء"
    ]
    bot.send_poll(chat_id=CHAT_ID, question=question, options=options, is_anonymous=False)
