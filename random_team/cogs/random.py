import numpy as np
from .utils.team import generate_teams, get_voice_channel, move_members, format_teams
from discord.ext import commands
from discord import client


class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shuffle', help='Splits players into 2 teams. And writes them to the chat.')
    async def split_players(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('You have to be in voice channel')
            return


        channel = ctx.author.voice.channel
        members = channel.members
        teams = generate_teams(members)
        names = [[m.name for m in team] for team in teams]
        await ctx.send(format_teams(names))


    shuffle_move_desc = """
    Splits players into 2 teams, moves 2nd team to selected channel.
    Channel can be chosen by name or index. By default moves to 1st voice channel
    """
    @commands.command(name='shuffle-move', help=shuffle_move_desc)
    async def shuffle_move(self, ctx, voice="1"):
        if ctx.author.voice is None:
            await ctx.send('You have to be in voice channel')
            return

        members = ctx.author.voice.channel.members
        teams = generate_teams(members)

        voice_channel = get_voice_channel(ctx, voice)

        if voice_channel:
            await move_members(self.bot, teams[0], voice_channel)
        names = [[m.name for m in team] for team in teams]
        await ctx.send(format_teams(names))

