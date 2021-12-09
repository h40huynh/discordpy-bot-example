from discordbot.bot import DiscordBOT
from discordbot.cog.ping import Ping

BOT_TOKEN = "OTE3NzQ2MjIyMzk4MzEyNDY4.Ya9Lxg.76QRuagbLSxe4fE7tivWt5I-ijY"
LOGGING_CHANNEL = 918300079880822855

bot = DiscordBOT(BOT_TOKEN, logging_channel_id=LOGGING_CHANNEL)
bot.add_cog(Ping(bot))
bot.start_bot()
