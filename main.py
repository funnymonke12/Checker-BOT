import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import API_TOKEN
from database import insert_username, get_usernames
from connect_trello import create_card




# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class Form(StatesGroup):
    username = State()
@dp.message_handler(commands=['Зарузить'])
async def insert_username(message: types.Message):
    await Form.username.set()
    await message.reply('Пользователь добавлен в отслеживаемых пользователей')

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(commands=['Отменить'], state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Заугрзка отменена')

@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.username in get_usernames():
        await message.answer(f"Вы, пользователь {message.from_user.username} отслеживаетесь")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)