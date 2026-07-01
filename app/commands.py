import random as r
import discord
from discord.ext import commands
import aiohttp
from config.settings import tokenApex

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)

    @commands.command()
    async def helpme(self, ctx):
        await ctx.send(
            """all my command:
            1) /test
            2) /help
    """)
        

    """ APEX LEGENDS API COMMANDS """
    @commands.command()
    async def apexmap(self, ctx):
        url = f"https://api.apexlegendsstatus.com/maprotation?auth={tokenApex}&version=2"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                else:
                    await ctx.send(f'error API: status {response.status}')
                    return
        mode = data.get('ranked', {})
        current = mode.get('current', {})
        next_map = mode.get('next', {})


        asset_url = current.get('asset')  # может быть None

        # ---- Embed 1: текущая карта с баннером ----
        embed_current = discord.Embed(
            title="🟢 Текущая карта",
            color=discord.Color.green()
        )
        embed_current.add_field(
            name="Карта",
            value=current.get('map', 'Неизвестно'),
            inline=False
        )
        embed_current.add_field(
            name="⏳ Осталось",
            value=current.get('remainingTimer', 'N/A'),
            inline=True
        )
        embed_current.add_field(
            name="⏱️ Длительность",
            value=f"{current.get('DurationInMinutes', '?')} мин.",
            inline=True
        )
        # Широкий баннер внизу
        if asset_url:
            embed_current.set_image(url=asset_url)

        # ---- Embed 2: следующая карта с баннером (используем ту же картинку) ----
        embed_next = discord.Embed(
            title="🔜 Следующая карта",
            color=discord.Color.blue()
        )
        embed_next.add_field(
            name="Карта",
            value=next_map.get('map', 'Неизвестно'),
            inline=False
        )
        embed_next.add_field(
            name="🕐 Начало в",
            value=next_map.get('readableDate_start', 'N/A'),
            inline=True
        )
        embed_next.add_field(
            name="⏱️ Длительность",
            value=f"{next_map.get('DurationInMinutes', '?')} мин.",
            inline=True
        )
        # Тот же баннер для второго Embed
        if asset_url:
            embed_next.set_image(url=asset_url)

        # Отправляем оба Embed в одном сообщении
        await ctx.send(embeds=[embed_current, embed_next])


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))