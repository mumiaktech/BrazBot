import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("Error: Token not found. Please set the TELEGRAM_BOT_TOKEN environment variable.")
    exit()

# Initialize the bot with the token
bot = Bot(token=TOKEN)

# Define an async function to get bot info
async def get_bot_info():
    bot_info = await bot.get_me()
    print(bot_info)

# Run the async function using asyncio
if __name__ == "__main__":
    asyncio.run(get_bot_info())
