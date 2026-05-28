import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")
CHANNEL_URL = "https://t.me/alextoto"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔥 Join my channel", url=CHANNEL_URL)]]
    await update.message.reply_text(
        "Hey! I'm Alex 🔥\n\nExclusive personalized content just for you.\n\nReady? 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
