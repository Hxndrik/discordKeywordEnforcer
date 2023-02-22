import discord
import os

from keep_alive import keep_alive

client = discord.Client()

# Configure dictionary of channel id's and their corresponding keywords here
channel_keywords = {
    1065711308164571237: ["pasta", "sauce", "cheese"],
    1065711265156177990: ["rice", "fried", "flower"]
}


# optional: logging in python console
@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    # check if message was sent in one of the specified channels
    if message.channel.id in channel_keywords:
        # check if message includes all keywords for that channel
        keywords = channel_keywords[message.channel.id]
        if not all(word.lower() in message.content.lower()
                   for word in keywords):
            # delete the message if not all of the keywords are in the message
            await message.delete()


@client.event
async def on_message_edit(before, after):
    # check if message was modified in one of the specified channels
    if after.channel.id in channel_keywords:
        # check if message includes all keywords for that channel
        keywords = channel_keywords[after.channel.id]
        if not all(word.lower() in after.content.lower() for word in keywords):
            # delete the message if not all of the keywords are in the message
            await after.delete()


print("Script is ready")
#To prevent the script from turning off
# Ping https with uptimerobot
keep_alive()

# Insert your bot secret-key here.
client.run(os.environ['secretkey'])
