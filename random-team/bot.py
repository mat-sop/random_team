from discord.ext import commands


bot = commands.Bot(command_prefix='$')


@bot.command(name='split', help='Splits players')
async def split_players(ctx):
    channel = ctx.author.voice.channel
    members = channel.members
    response = [member.name for member in members]

    await ctx.send(response)


bot.run('Njc4NjAyMjQ3NzA5NTI0MDI0.Xkld3w.J5oBjxiAmIC6Wf-JowlIJIX9ovk')
