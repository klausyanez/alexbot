import asyncio
import os
import httpx

TOKEN = "8975271983:AAExvEKDjm8mhI7A2BmYpsGIhA7ZZ-rb7j4"
CHANNEL_URL = "https://t.me/alextoto7"
API = f"https://api.telegram.org/bot{TOKEN}"

async def get_updates(offset=None):
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    async with httpx.AsyncClient(timeout=40) as client:
        r = await client.get(f"{API}/getUpdates", params=params)
        return r.json()

async def send_message(chat_id, text, keyboard=None):
    data = {"chat_id": chat_id, "text": text}
    if keyboard:
        data["reply_markup"] = keyboard
    async with httpx.AsyncClient() as client:
        await client.post(f"{API}/sendMessage", json=data)

async def main():
    print("Bot started!")
    offset = None
    while True:
        try:
            result = await get_updates(offset)
            for update in result.get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message", {})
                text = msg.get("text", "")
                chat_id = msg.get("chat", {}).get("id")
                if text == "/start" and chat_id:
                    keyboard = {
                        "inline_keyboard": [[
                            {"text": "🔥 Join my channel", "url": CHANNEL_URL}
                        ]]
                    }
                    await send_message(
                        chat_id,
                        "Hey! I'm Alex 🔥\n\nExclusive personalized content just for you.\n\nReady? 👇",
                        keyboard
                    )
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(5)

asyncio.run(main())
