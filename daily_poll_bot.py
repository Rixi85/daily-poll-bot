from telegram import Bot, Poll, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import time
import logging

# ==========================
BOT_TOKEN = '7599034036:AAHoltCH4gvuUxnxItsi-gL6yQ8FvfQ6GYM'
YOUR_CHAT_ID = 6393012286  # استبدله بالـ chat ID الخاص بك
# ==========================

# إعدادات السجل
logging.basicConfig(level=logging.INFO)

# المهام اليومية
daily_tasks = [
    "أذكار الصباح",
    "التسبيح",
    "الإستغفار",
    "الصلاة على النبي",
    "لا اله الا الله والله اكبر",
    "لا اله الا الله وحده",
    "لا اله الا الله ولا شريك له",
    "لا اله الا الله ولا حول ولا قوة الا بالله",
    "أذكار المساء"
]

def send_daily_poll(context: CallbackContext):
    bot: Bot = context.bot
    bot.send_poll(
        chat_id=YOUR_CHAT_ID,
        question="📿 ماذا أنجزت من أذكارك اليوم؟",
        options=daily_tasks,
        is_anonymous=False,
        allows_multiple_answers=True
    )

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 تم تفعيل بوت الأذكار! سيتم إرسال المهام يوميًا الساعة 5 صباحًا بإذن الله.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    job_queue = updater.job_queue
    job_queue.run_daily(
        send_daily_poll,
        time=time(hour=5, minute=0)  # الساعة 5 صباحًا
    )

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
