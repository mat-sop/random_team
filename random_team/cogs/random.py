from discord import client
from discord.ext import commands

from .utils.team import (filter_bots, generate_teams, get_voice_channel,
                         move_members)


class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    shuffle_help = 'Takes list of voice channels. Splits players evenly into given channels.'
    @commands.command(name='shuffle', help=shuffle_help)
    async def shuffle(self, ctx, *args):
        if ctx.author.voice is None:
            await ctx.send('You have to be in voice channel')
            return

        members = filter_bots(ctx.author.voice.channel.members)
        print(f'members : {members}')

        voice_channels = [get_voice_channel(ctx, voice_name) for voice_name in args]
        print(f'voice_channels: {voice_channels}')
        teams = generate_teams(members, len(voice_channels))
        print(f'teams: {teams}')

        text_output = ''

        for team, voice_channel in zip(teams, voice_channels):
            await move_members(self.bot, team, voice_channel)
            team_names = ', '.join([member.nick if member.nick else member.name for member in team])
            text_output += f'{voice_channel.name}:\n{team_names}\n\n'

        await ctx.send(text_output)
