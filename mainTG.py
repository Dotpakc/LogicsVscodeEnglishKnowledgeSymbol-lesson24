import asyncio
import logging
import re
import json


from random import choice
from decouple import config


from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.utils import keyboard
from aiogram.filters import CommandStart, Command   
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

TOKEN = config("TOKEN")

dp = Dispatcher() # объект диспетчера (оброботчик событий)
bot = Bot(TOKEN)


#MENU
mainmenu = keyboard.InlineKeyboardBuilder()
mainmenu.row(types.InlineKeyboardButton(text="🎮Випадкова Гра", callback_data="random_game"))



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привіт! Я бот для пошуку ігор на Metacritic",reply_markup=mainmenu.as_markup())





async def main() -> None:
    await bot.set_my_commands([], scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())