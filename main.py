#모듈 불러오기_1
import os
from dotenv import load_dotenv

#토큰 (.env 파일 생성 필수!)
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#모듈 불러오기_2
import discord
from discord.ext import commands

#Intents 활성화
INTENTS = discord.Intents.all()

#Bot 세팅 및 jishaku 불러오기
bot = commands.Bot(command_prefix=">", intents=INTENTS)
bot.load_extension('jishaku')


#./cogs 폴더 불러오기
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[-3]}')


#봇 구동하기!
bot.run(token)