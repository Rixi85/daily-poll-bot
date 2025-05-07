import os
from flask import Flask, request
from telegram import Bot
import datetime

# ✅ Correct way to get values from environment variables
TOKEN = os.getenv("7599034036:AAHoltCH4gvuUxnxItsi-gL6yQ8FvfQ6GYM")
CHAT_ID = os.getenv("6393012286")

# ✅ Initialize bot with the token
bot = Bot(token=TOKEN)

# ✅ Initialize Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running with webhook!"

@app.route("/webhook", methods=["POST"])
def webhook():
    # ✅ When webhook is triggered (e.g. by cron job), send the poll
    send_daily_poll()
    return "ok", 200

def send_daily_poll():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    question = f"What are your main tasks for today? ({today})"
    options = ["Client editing", "Studio shoot", "Location shoot", "Backups", "Retouching"]

    # ✅ Send the poll to your chat ID
    bot.send_poll(
        chat_id=CHAT_ID,
        question=question,
        options=options,
        is_anonymous=False
    )

if __name__ == "__main__":
    app.run()
