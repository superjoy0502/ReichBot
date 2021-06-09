# -*- coding: utf-8 -*-

import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check


class Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="핑")
    async def ping(self, ctx):
        await ctx.send('퐁 {0}ms'.format(round(self.bot.latency * 1000)))

    @commands.command(name="생성")
    async def create(self, ctx):
        await ctx.send("국가 생성 완료")


def setup(bot):
    bot.add_cog(Commands(bot))
