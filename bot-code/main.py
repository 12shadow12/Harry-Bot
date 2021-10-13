import discord
import os
import random

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


    msg = message.content

    if msg.startswith('hello'):
      await message.channel.send('you do not have enough testosterone doode')

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(crying_gifs))

    if msg.startswith('sleep'):
      await message.channel.send('sleep is for the gay')

    if msg.startswith('https://youtu.be/'):
      await message.channel.send('your videos are gay mate, smoke some testosterone')

    if msg.startswith('https://www.youtube.com/'):
      await message.channel.send('your videos are gay mate, smoke some testosterone')


client.run(os.getenv('TOKEN'))
