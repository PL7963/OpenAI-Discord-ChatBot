import discord
import os
from openai_response import response

user_response = ""
#CONFIG'
TOKEN = ''  ####TYPE YOUR DISCORD TOKEN HERE####

intents = discord.Intents.all()
CHANNEL=[]  #The channels that bot can talk
#CONFIG


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("You're now logged in as {0.user}".format(client))
    os.environ["STARTUP"] = "0"

@client.event
async def on_message(message):
    if message.channel.id not in CHANNEL: #Add change "in" to "not in" if you want let AI only not talk at the channels you set
        if message.author == client.user:
            return
        else:
            if message.content.startswith("!"):
                async with message.channel.typing():
                    user_response = message.content
                    await message.channel.send(response(user_response))
client.run(TOKEN)
