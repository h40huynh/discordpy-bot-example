from discord.ext import commands

ALLOWED_CHANNELS = [911081579550494742]


async def is_allowed_channel(ctx):
    if ALLOWED_CHANNELS is None:
        return True
    return ctx.channel.id in ALLOWED_CHANNELS


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', description='Check bot is alive.')
    @commands.check(is_allowed_channel)
    async def ping(self, ctx):
        await ctx.send('Pong!')
