import os

from discord.ext import commands

from cogs.lol import League_of_Legends
from cogs.random import Random

bot_description = 'Bot that splits members into teams.'
bot = commands.Bot(command_prefix='$rng ', description=bot_description)

bot.add_cog(Random(bot))

token = os.getenv('DISCORD_BOT_TOKEN', '')
bot.run(token)
