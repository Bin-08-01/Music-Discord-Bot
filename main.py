import discord
from discord.ext import commands
import Bot
from discord.utils import get

cogs = [Bot]

def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

client = commands.Bot(command_prefix='#', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTM2MjM0Njk2NDkxMjcwMjE0.YfKOgg.Qp4ZvfGS8ohTiogKnrgJPnB9OTM")
