import logging
import datetime
import pytz
from telegram import Bot
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = '7599034036:AAHoltCH4gvuUxnxItsi-gL6yQ8FvfQ6GYM'  # Replace this with your actual bot token
CHAT_ID = '6393012286'  # Replace with your personal Telegram chat ID

logging.basicConfig(level=logging.INFO)

# Your daily tasks
TASKS = [
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

async def send_daily_poll(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_poll(
        chat_id=CHAT_ID,
        question="🕌 *Your Daily Spiritual Tasks*",
        options=TASKS,
        allows_multiple_answers=True,
        is_anonymous=False,
        parse_mode=ParseMode.MARKDOWN
    )

async def start_command(update, context):
    await update.message.reply_text("✅ Auto poll bot is running and will send daily tasks.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))

    scheduler = BackgroundScheduler()
    saudi_time = pytz.timezone('Asia/Riyadh')

    scheduler.add_job(
        lambda: app.create_task(send_daily_poll(ContextTypes.DEFAULT_TYPE(bot=Bot(token=TOKEN)))), 
        'cron', hour=17, minute=41, timezone=saudi_time
    )

    scheduler.start()
    app.run_polling()

if __name__ == '__main__':
    main()
