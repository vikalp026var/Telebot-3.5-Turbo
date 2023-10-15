import logging
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os 

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
# print(API_TOKEN)

#######configure logging
logging.basicConfig(level=logging.INFO)
##Initialize bot and dispatcher


bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)




@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    "This handler receives message with '/start" 'or' '/help'
    await message.reply("Hi\n I am Echo Bot!\n Made by Vikalp(Zhcet).")




@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo"""
    await message.answer(message.text)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)