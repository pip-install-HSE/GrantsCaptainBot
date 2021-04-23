from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils import executor

import keyboards
import messages
from config import dp, bot
from states import Registration


@dp.message_handler(commands=['start'])
async def handle_start_cmd(message: types.Message):
    await message.answer('Приветственное сообщение. Отправьте свой регион')
    await Registration.Region.set()


@dp.message_handler(state=Registration.Region)
async def get_region(message: types.Message, state: FSMContext):
    # Запись данных в бд
    await message.answer('От лица кого планируете подавать заявки?', reply_markup=keyboards.get_face_keyboard())
    await Registration.Face.set()


@dp.callback_query_handler(text_contains='face', state=Registration.Face)
async def get_face_choice(callback: CallbackQuery, state: FSMContext):
    await Registration.Support.set()
    face = callback.data.split('_')[1]
    # Запись face в бд
    await bot.send_message(callback.message.chat.id,
                           f'Направление поддержки в конкурсе по которому хотите получать анонсы',
                           reply_markup=keyboards.get_support_keyboard())


@dp.callback_query_handler(text_contains='support', state=Registration.Support)
async def get_support_type(callback: CallbackQuery, state: FSMContext):
    support_type = callback.data.split('_')[1]
    # Запись support_type в бд
    available_grants = 'Some available grants'  # Запрос к апи
    await state.reset_state()
    await bot.send_message(callback.message.chat.id, available_grants, reply_markup=keyboards.get_permanent_keyboard())


@dp.message_handler()
async def get_msg(message: types.Message):
    if message.text == 'О проекте':
        return await message.answer(messages.ABOUT_PROJECT)
    elif message.text == 'Поддержать проект':
        return await message.answer(messages.DONATE_LINKS)


@dp.message_handler(commands=['help'])
async def handle_help_cmd(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
