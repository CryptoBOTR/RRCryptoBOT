import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="🧮 Відкрити калькулятор", web_app=WebAppInfo(url="https://cryptobotr.github.io/RRCryptoBOT/"))
    )
    await message.answer("👋 Привіт!
Це бот для розрахунку Risk/Reward.
Натисни кнопку нижче:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)