import os
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
  print("Hello {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  adjective = ["fat", "chunky", "poop4", "chungus", "amongus","scarfmon","obamacare","fat","ugly","short","skinny","unpoggers", "unbased","bluepilled","sponchating","genshinimpact playing", "cringe", "league of legends playing", "stupid", "sussy"]

  verb = ["poop her pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
  "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
  "ate chungus juice", "walks her dog upside down", "uefduweudwe28du2882du82u8de2uued poop4", "poop4", "became a ManfaceBot contributor"]

  if message.content.startswith("-ym") or message.content.startswith("-yomama"):
    await message.channel.send("Yo mama is so " + random.choice(adjective) + " she " + random.choice(verb) + "!")
  if message.content.startswith("-yd") or message.content.startswith("-yodad"):
    await message.channel.send("Yo dad is so " + random.choice(adjective) + " he " + random.choice(verb) + "!")

my_secret = os.environ['token']
client.run(my_secret)

