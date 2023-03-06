from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6197159674:AAH7P8dPsMGfNoL7cwdeHSLddcSDjO0perw'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_commands(message: types.Message):
    await message.reply(text='HELP_COMMAND')

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
    await message.answer(text='Добро пожаловать в наш телеграм Бот!')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
