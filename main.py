import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from database import insert_username
from connect_trello import create_card

lst_tracked_users = ["funkymonjey"]


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.username in lst_tracked_users:
        await message.answer(f"Вы, пользователь {message.from_user.username} отслеживаетесь")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)