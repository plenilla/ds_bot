import discord
from config.settings import token 


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Ботиак запущен дорогой {self.user} пользователь')
        await self.close()

client = MyClient(intents=discord.Intents.default())
client.run(token)