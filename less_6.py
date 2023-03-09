from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6197159674:AAH7P8dPsMGfNoL7cwdeHSLddcSDjO0perw'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/help</b> - <em>показывает список команд</em>
<b>/give</b> - <em>отправляет стикеры</em>
<b>/start</b> - <em>запускает бота</em>'''


async def on_startup(_):
    print('Я запустился')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')


# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=str(message.text.count('✅')))


# @dp.message_handler(commands=['give'])
# async def send_sticker(message: types.Message):
#     await message.answer('Смотри какой котик ❤️')
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIBcdkBY_d_yJYkaw5eR0U6MTTYrLTowACiREAAjyzxQd3XR46Pa5Dbi4E')
#
#
# @dp.message_handler()
# async def send_sticker(message: types.Message):
#     if message.text == '❤️':
#         await message.answer('🖤')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup )
