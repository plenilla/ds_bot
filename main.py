import discord 
from discord.ext import commands
from config.settings import token 
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def main():
    await bot.load_extension('app.commands')
    await bot.start(token)

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

if __name__ == "__main__":
    asyncio.run(main())

