import os
import time

import discord
from discord.ext import commands

import watchsama



#TODO: Choicing random anime feature
#Add timeout
#Add description to first <br>

#Needs to have a single track reroll thats tracked with date
#Should I synthesize or make from a cached list
#----------------------------------------------------------------------------------
print('''
     __      __         __         .__                _________                      
    /  \    /  \_____ _/  |_  ____ |  |__            /   _____/____    _____ _____   
    \   \/\/   /\__  \\\   __\/ ___\|  |  \   ______  \_____  \\\__  \  /     \\\__  \  
     \        /  / __ \|  | \  \___|   Y  \ /_____/  /        \/ __ \|  Y Y  \/ __ \_
      \__/\  /  (____  /__|  \___  >___|  /         /_______  (____  /__|_|  (____  /
           \/        \/          \/     \/                  \/     \/      \/     \/ 
       by keopi#4078 |
    ''')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print("Connected to discord API")

    usable_emotes: discord.Guild = bot.get_guild(1103400705995329566).emojis
    

    watchsama.cogs.cmds.__init__(bot)
    await watchsama.cogs.mal.MAL.cog_setup(bot)

    #TODO: find a way to cache the range so u dont wanna die

    print(bot.guilds)
    check_file = os.stat('watchsama/cogs/mal/JSON/anime_data.json').st_size
    if check_file == 0 or check_file == 2:
        watchsama.cogs.mal.API.MALSelenium.cache_anime_meta()
        print("Creating embeds json")
    await bot.get_guild(1103400705995329566).text_channels[0].send('Watch-sama is running') #Find out how to get her to talk properly

    await bot.change_presence(status = discord.Status.online)


try:

    bot.run(watchsama.config.bot_token())

except Exception as e:
    print(f"[/!\\] Error: Failed to connect to DiscordAPI. Please check your bot token!\n{e}")
    time.sleep(5)
    exit(1)

#TODO: find a way to implement into the file structure instead of the bot connection
def get_emotes(): 
    emojis = bot.get_guild(1103400705995329566).emojis
    return emojis