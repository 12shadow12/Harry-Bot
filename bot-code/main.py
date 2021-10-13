import discord
import os
import random
import sys

print('Python Version:',sys.version[0:6])

client = discord.Client()

sad_words = ["fk u", "no u", "shyt", "nigger", "ghey", "nigga", "gay", "fking"]

crying_gifs = ["https://media.discordapp.net/attachments/809956725943566336/890364824352088074/855999071511511072.gif", "what did you just say doode?","https://c.tenor.com/aySvKBn5tAgAAAAM/anime.gif", "Get some brotein bro", "https://cdn.discordapp.com/emojis/868985496875991081.gif?size=32"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client:
      return

    username = str(message.author.name)  
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if client.user.mentioned_in(message):
      await message.channel.send('LoCaL IdIoTs SpAm PiNg ' + f'{message.author.mention}')

    msg = message.content

    if msg.startswith('hello'):
      await message.channel.send('you do not have enough testosterone doode')

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(crying_gifs))

    if msg.startswith('sleep'):
      await message.channel.send('sleep is for the gay')

    if msg.startswith('https://www.youtube.com/'):
      await message.channel.send('your videos are trash mate, smoke some testosterone')

    if msg.startswith('fag'):
      await message.channel.send('sorry, ' + f'{username} ' + 'this is a christian server and we dont use words like that', file=discord.File('pooh.jpg'))

    # React to Embeds
    



client.run(os.getenv('TOKEN'))
