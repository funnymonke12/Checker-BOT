from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN
import database as db
from connect_trello import create_card, get_listID
from keyboard import basic_kb, cancel_kb


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    username = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('В этом боте вы можете загрузить людей для проверки их сообщений в чатах'\
                         ,reply_markup=basic_kb)
@dp.message_handler(commands=['Загрузить'])
async def insert_username(message: types.Message):
    await Form.username.set()
    await message.answer("Напишите имя пользователя контрагента", reply_markup=cancel_kb)

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
    await message.reply('Заугрзка отменена', reply_markup=basic_kb)

@dp.message_handler(state=Form.username)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        data['username'] = message.text

    await message.answer('Данные загружен в БД', reply_markup=basic_kb)
    await db.sql_add_command(state)
    await state.finish()

@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.username in db.get_usernames() and 'склад' in message.text.lower():
        await message.answer('Создаю карточку в Trello')
        # lstID = get_listID()
        # create_card(lstID)


        print('yes')
async def on_startup(_):
    print('Бот подключился')
    db.sql_start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)