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

        # Создаём Embed
        embed = discord.Embed(
            title="🗺️ Ротация карт Apex Legends",
            color=discord.Color.gold()
        )

        # Блок с текущей картой
        embed.add_field(
            name="🟢 Текущая карта",
            value=(
                f"**Карта:** {current.get('map', 'Неизвестно')}\n"
                f"**🕐 Начало в:** {current.get('readableDate_start', 'N/A')}\n"
                f"**🕐 Конец в **{current.get('readableDate_end', 'N/A')}\n"
                f"**⏳ Осталось:** {current.get('remainingTimer', 'N/A')}\n"
                f"**⏱️ Длительность:** {current.get('DurationInMinutes', '?')/60} ч."
            ),
            inline=False
        )

        # Блок со следующей картой
        embed.add_field(
            name="🔜 Следующая карта",
            value=(
                f"**Карта:** {next_map.get('map', 'Неизвестно')}\n"
                f"**🕐 Начало в:** {next_map.get('readableDate_start', 'N/A')}\n"
                f"**🕐 Конец в **{next_map.get('readableDate_end', 'N/A')}\n"
                f"**⏱️ Длительность:** {next_map.get('DurationInMinutes', '?')/60} ч."
            ),
            inline=False
        )

        # Устанавливаем иконку текущей карты (справа сверху)
        asset_url = current.get('asset')
        if asset_url:
            embed.set_thumbnail(url=asset_url)

        embed.set_footer(text="Данные от ApexLegendsStatus.com")

        await ctx.send(embed=embed)


    @commands.command()
    async def random(self, ctx, max_value: int):
        number = r.randint(1, max_value)
        await ctx.send(f"Случайное число от 1 до {max_value}: \n **{number}**")


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))