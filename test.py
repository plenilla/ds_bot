import discord
from config.settings import token 


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.close()

client = MyClient(intents=discord.Intents.default())
client.run(token)