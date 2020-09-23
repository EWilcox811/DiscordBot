import os
import discord
import random
import time
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

# server id = 756657210087571466
messages = 0
joined = 0

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix = '.')

print(discord.__version__)

## This is a background task that updates the Stats.txt file automatically every 60 seconds.
## It adds the time, number of messages and the number of members joined within that 60 second
## timeframe.  If no one sends a message or joins in that timeframe it will print 0 to the file.
# async def update_stats():
#     await client.wait_until_ready()
#     global messages, joined
#
#     while not client.is_closed():
#         try:
#             with open("stats.txt", "a") as f:
#                 f.write(f"Time:  {int(time.time())}, Messagess: {messages}, Members Joines: {joined}\n")
#             messages = 0
#             joined = 0
#
#             await asyncio.sleep(60)
#         except Exception as e:
#             print(e)
#             await asyncio.sleep(60)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!\n{discord.__version__}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['As i see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook is not so good.',
                 'Outlook good.',
                 'Reply hazy, try again',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes - definitely.',
                 'You may rely on it.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

# @client.command()
# async def kick(ctx, member : discord.Member, *, reason = None):
#     await member.kick(reason = reason)
#
# @client.command()
# async def ban(ctx, member : discord.Member, *, reason = None):
#     await member.ban(reason = reason)


client.run(TOKEN)
