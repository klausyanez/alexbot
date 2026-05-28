import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8975271983:AAExvEKDjm8mhI7A2BmYpsGIhA7ZZ-rb7j4")
CHANNEL_URL = "https://t.me/alextoto7"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔥 Join my channel", url=CHANNEL_URL)]]
    await update.message.reply_text(
        "Hey! I'm Alex 🔥\n\nExclusive personalized content just for you.\n\nReady? 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()
