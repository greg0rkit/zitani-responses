# bot.py
import os

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='%', intents = intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name==GUILD:
            break
    
    print(
        f'{bot.user.name} is connected to the following guild: \n'
        f'{guild.name}\n'
    )
    print(
        f'Amount of members: {guild.member_count}\n'
    )

@bot.command(name="zn")
async def pinging_bot(ctx):
    await ctx.channel.send("kariolh mh ta valeis me emas")

#@bot.command(name="print")
#async def print(ctx, args):
#    await ctx.channel.send(args)



bot.run(TOKEN)