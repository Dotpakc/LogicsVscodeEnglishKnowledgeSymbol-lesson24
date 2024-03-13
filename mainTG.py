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
#WEB APP


TOKEN = config("TOKEN")

dp = Dispatcher() # объект диспетчера (оброботчик событий)
bot = Bot(TOKEN)


#MENU
mainmenu = keyboard.InlineKeyboardBuilder()
mainmenu.row(types.InlineKeyboardButton(text="Пошук ігор", web_app=types.WebAppInfo(url="https://lol.ithillelcraft.com/tg")))



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привіт! Я бот для пошуку ігор на Metacritic",reply_markup=mainmenu.as_markup())

@dp.message()
async def web_app_handler(message: types.Message):
    print(message.web_app_data)
    await message.answer(message.web_app_data)



async def main() -> None:
    await bot.set_my_commands([], scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())