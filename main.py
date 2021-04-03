import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='~', description='Jeeves, the A:NR Discord Bot')
extensions = ['cogs.cards']

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))

# GET - https://netrunnerdb.com/api/2.0/public/cards
# GET - https://netrunnerdb.com/api/2.0/public/mwl