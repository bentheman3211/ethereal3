import discord


import time
import os

import logging
import threading

from discord.ext import commands
import asyncio
msg = msg = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[:rocket:Ethereal Advertising:rocket:]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n> :money_with_wings: Free, fast, and easy advertising!\n> :heart: Cheap promotions to help your server grow! \n> :mag: Insight on how to grow and manage an social media platform! \n> :game_die: **THE BEST PART** We reward you to advertise your server with shout-outs and auto advertisements! \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**So what is our goal?** Our goal is to teach people how to manage and grow a community. Anyone can hit 'Create server', but without the knowlegde of creating a server, comes with failure. I, the owner of Ethereal have experienced this many times, but I bet if someone challenged me, **I can grow a server to 100 members on any server!**\n**Whats in it for you?** Well, you can learn a lot from successful people, right? We can easily teach you our tactics and tricks! Our goal is that you can not only advertise but learn from our server. And learn what works, and what doesn't! \n Join now: https://discord.gg/ChhB4FQESF"


client = commands.Bot(command_prefix="!", self_bot=True, help_command=None, intents=discord.Intents.all())

token ="MTAzMzQ3MTU1ODMzMDYyMjAxNA.Gt2ow-.1zl7oGWwwC6AHPq-752yu2t2f-O0Zp4ml7pb5I"




async def task1():
  await asyncio.sleep(1)
  while True:
    await client.wait_until_ready()
    channel = await client.fetch_channel(1035254700825661503)
    await channel.send(msg)
    print(" msg  1")
    await asyncio.sleep(5)



















@client.event
async def on_ready():
  print("The bot is ready")

  client.loop.create_task(task1())
  





TOKEN = os.environ.get(token)
client.run(token, bot=False)
