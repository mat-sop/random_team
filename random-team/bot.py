import numpy as np
from discord.ext import commands
from team import format_teams, split_members
import os

bot = commands.Bot(command_prefix='$rng ')


@bot.command(name='shuffle', help='Splits players into 2 teams.')
async def split_players(ctx, teams_number: int=2):
    if ctx.author.voice is None:
        await ctx.send('You have to be in voice channel')
        return

    channel = ctx.author.voice.channel
    members = channel.members
    teams = split_members(members, teams_number)
    response = format_teams(teams)

    await ctx.send(response)


token = os.getenv('DISCORD_BOT_TOKEN', '')
bot.run(token)
