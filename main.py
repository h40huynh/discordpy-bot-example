from discordbot.bot import DiscordBOT
from discordbot.cog.ping import Ping

BOT_TOKEN = ""
LOGGING_CHANNEL = 918300079880822855

bot = DiscordBOT(BOT_TOKEN, logging_channel_id=LOGGING_CHANNEL)
bot.add_cog(Ping(bot))
bot.start_bot()
