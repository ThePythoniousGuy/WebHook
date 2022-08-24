import asyncio
import html
import logging
import os
from dataclasses import dataclass
from http import HTTPStatus
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import *



key = "5731648931:AAEwLrkdTUwQukOGMsjw5GyUV7EcytlCI8I" # Changed a bit so it wont work! :P


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(u,c) -> None:
    """Display a message with instructions on how to use this bot."""
    url = c.bot_data["url"]
    text = "Hello"
    await u.message.reply_html(text=text)



async def main() -> None:
    """Set up the application and a custom webserver."""
    url = "https://webhook-ptb.herokuapp.com"
    admin_chat_id = 5221243716
    port = int(os.environ.get('PORT', '8443'))
    print(port)
    print(os.environ.get('$PORT'))

    TOKEN = key
    app = ApplicationBuilder().token(key).build()
    
    app.bot_data["url"] = url
    app.bot_data["admin_chat_id"] = admin_chat_id

    # register handlers
    app.add_handler(CommandHandler("start", start, block=False))
    
    app.run_webhook(listen="0.0.0.0", port=port, url_path=TOKEN,webhook_url=f"{url}/{TOKEN}")
if __name__ == "__main__":
    asyncio.run(main())
