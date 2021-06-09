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


bot.load_extension("commands")


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
