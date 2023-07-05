from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_input = KeyboardButton('/Загрузить')
basic_kb = ReplyKeyboardMarkup(resize_keyboard=True)
basic_kb.add(button_input)

button_cancel = KeyboardButton('/Отменить')
cancel_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
cancel_kb.add(button_cancel)