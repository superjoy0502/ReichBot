# -*- coding: utf-8 -*-

import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check

bot = commands.Bot(command_prefix="//")


@bot.event
async def on_ready():
    print("bot online")


@bot.command(name="핑")
async def ping(ctx):
    await ctx.send('퐁 {0}ms'.format(round(bot.latency*1000)))


@bot.command(name="생성")
async def create(ctx):
    await ctx.send("국가 생성 완료")


bot.run(os.getenv("TOKEN"))
