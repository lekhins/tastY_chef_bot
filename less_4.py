from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6197159674:AAH7P8dPsMGfNoL7cwdeHSLddcSDjO0perw'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

import string
import random

count = 0


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer('Этот бот умеет отправлять рандомные  символы алфавита')
    await message.delete()


@dp.message_handler(commands=['count'])
async def check_out(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1


@dp.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp)
