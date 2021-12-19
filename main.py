import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=">")
bot.load_extension('jishaku')



bot.run(token)