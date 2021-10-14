import discord
from discord.ext import commands
import os
import random
import sys

print('Python Version:',sys.version[0:6])

client = commands.Bot(command_prefix = '!')

sad_words = ["fk u", "no u", "shyt", "nigger", "ghey", "nigga", "gay", "fking", "fuck", "Fuck", "suck my", "ass", "dick"]

crying_gifs = ["https://media.discordapp.net/attachments/809956725943566336/890364824352088074/855999071511511072.gif", "what did you just say doode?","https://c.tenor.com/aySvKBn5tAgAAAAM/anime.gif", "Get some brotein bro", "https://cdn.discordapp.com/emojis/868985496875991081.gif?size=32"]

emojis = [896284438592385035, 892166330533433385, 840506809717882890, 891095263211581450, 882476300810481677, 839389367231184907]

@client.command(pass_context = True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I left the voice channel")
  else:
    await ctx.send("I am not in a voice channel")
  
@client.command()
async def hello(ctx):
  await ctx.send("hi")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return
  if len(message.embeds) != 0:
    await message.add_reaction(client.get_emoji(random.choice(emojis)))


  await client.process_commands(message)

  username = str(message.author.name)  
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if client.user.mentioned_in(message):
    await message.channel.send('LoCaL IdIoTs SpAm PiNg ' + f'{message.author.mention}')

  msg = message.content

  if msg.startswith('hello'):
    await message.channel.send('you do not have enough testosterone doode')

  elif any(word in msg for word in sad_words):
    await message.channel.send(random.choice(crying_gifs))

  elif msg.startswith('sleep'):
    await message.channel.send('sleep is for the gay')

  elif msg.startswith('fag'):
    await message.channel.send('sorry, ' + f'{username} ' + 'this is a christian server and we dont use words like that', file=discord.File('pooh.jpg'))

    # React to Embeds


client.run(os.getenv('TOKEN'))
