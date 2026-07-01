import discord 
from discord.ext import commands
import random as r
from config.settings import token 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def helpme(ctx):
    await ctx.send(
        """all my command:
        1) /test
        2) /help
""")


@bot.command()
async def random(ctx, max_value: int):
    number = r.randint(1, max_value)
    await ctx.send(f"Случайное число от 1 до {max_value}: \n **{number}**")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send('Hello')

    await bot.process_commands(message)

bot.run(token)

