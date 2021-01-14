import os

from discord.ext import commands

from cogs.random import Random
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

bot_description = 'Bot that splits members into teams.'
bot = commands.Bot(command_prefix='$rng ', description=bot_description)

bot.add_cog(Random(bot))

bot.run(token)
