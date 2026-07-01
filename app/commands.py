import random as r
import discord
from discord.ext import commands


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


    @commands.command()
    async def random(self, ctx, max_value: int):
        number = r.randint(1, max_value)
        await ctx.send(f"Случайное число от 1 до {max_value}: \n **{number}**")


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))