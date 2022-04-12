import lightbulb
import hikari
import random
import time
import asyncio
import os
from dotenv import load_dotenv
# used to open the file containing your discord bot token
load_dotenv()
bot = lightbulb.BotApp(
    token= os.getenv('DISCORD_TOKEN'),
    default_enabled_guilds=(963463443220947026))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot has started!")


# Ping Command that responds with pong and the user's Ping
# The order of these decorators is important
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f'Pong!')

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand.')

@bot.command
@lightbulb.option('num2', 'The first number', type=int)
@lightbulb.option('num1', 'The second number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@bot.command
@lightbulb.option('question', 'Question asked')
@lightbulb.command('eightball', 'Shake the magic 8 ball.')
@lightbulb.implements(lightbulb.SlashCommand)
async def eightBall(ctx):
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
    await ctx.respond(ctx.options.question + f'\nAnswer:\t\t{random.choice(responses)}')
bot.run()
