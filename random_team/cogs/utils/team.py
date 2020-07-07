import random
from typing import List

import numpy as np
from discord import ChannelType, client


def filter_bots(members: List) -> List:
    return [member for member in members if not member.bot]


def generate_teams(members: List, number_of_teams: int):
    random.shuffle(members)
    return [list(team) for team in np.array_split(members, number_of_teams)]


def get_channel_by_name(channels, name):
    for c in channels:
        if c.name == name:
            return c
    return None


def get_channel_by_position(channels, index):
    for c in channels:
        if c.position == index:
            return c
    return None


def get_voice_channel(ctx, arg):
    channels = ctx.guild.voice_channels
    c = get_channel_by_name(channels, arg)
    if c is None and arg.isdigit():
        c = get_channel_by_position(channels, int(arg)-1)
    return c


async def move_members(bot, members, channel):
    for m in members:
        await m.move_to(channel)
