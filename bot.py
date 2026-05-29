import asyncio
import httpx

TOKEN = "8975271983:AAExvEKDjm8mhI7A2BmYpsGIhA7ZZ-rb7j4"
CHANNEL_URL = "https://t.me/alextoto7"
API = f"https://api.telegram.org/bot{TOKEN}"

async def send_animation(chat_id, gif_id, caption, keyboard=None):
    data = {"chat_id": chat_id, "animation": gif_id, "caption": caption}
    if keyboard:
        data["reply_markup"] = keyboard
    async with httpx.AsyncClient() as client:
        await client.post(f"{API}/sendAnimation", json=data)

async def get_updates(offset=None):
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    async with httpx.AsyncClient(timeout=40) as client:
        r = await client.get(f"{API}/getUpdates", params=params)
        return r.json()

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

                # Log any animation/document received
                if "animation" in msg:
                    file_id = msg["animation"]["file_id"]
                    print(f"ANIMATION FILE_ID: {file_id}")
                if "document" in msg:
                    file_id = msg["document"]["file_id"]
                    print(f"DOCUMENT FILE_ID: {file_id}")

                if text == "/start" and chat_id:
                    keyboard = {
                        "inline_keyboard": [[
                            {"text": "🔥 Join my free channel", "url": CHANNEL_URL}
                        ]]
                    }
                    await send_animation(
                        chat_id,
                        "https://i.imgur.com/kBqJ8p3.gif",
                        "Hey 👋 I'm Alex — Latin model from Colombia 🇨🇴\n\n"
                        "I share exclusive content on my free channel.\n"
                        "Hot photos, videos and more 🔥\n\n"
                        "Join now and see what's waiting for you 👇",
                        keyboard
                    )
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(5)

asyncio.run(main())
