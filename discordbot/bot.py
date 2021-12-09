import discord
from discord.ext import commands


class DiscordBOT(commands.Bot):
    def __init__(self, token: str, logging_channel_id: int = 0) -> None:
        super().__init__(command_prefix="!")
        self.token = token
        self.logging_channel_id = logging_channel_id

    async def on_ready(self) -> None:
        self.logging_channel = self.get_channel(self.logging_channel_id)
        print('[+] DiscordBOT is starting...')
        print(f'[+] Found logging channel: {self.logging_channel}')

    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return
        await self.process_commands(message)

    async def on_command(self, ctx):
        await self.command_logging(ctx)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        # Logging error command
        await self.logging_channel.send(f'[x] {ctx.author} fail on command {ctx.command}')

    async def command_logging(self, ctx) -> None:
        await self.logging_channel.send(
            f'[+] Command {ctx.command} was executed by {ctx.author}')

    def start_bot(self) -> None:
        self.run(self.token)
