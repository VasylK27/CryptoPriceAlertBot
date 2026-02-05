import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
