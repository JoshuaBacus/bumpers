import discord, os, time
from discord.ext import commands


# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
#token = os.getenv("TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
#token = "NzI3NTMwNDg5NzM2NDYyMzc4.XvtLpw.cuBm-sButb8hzLSeRAz6mQfgRc4"

bot = commands.Bot(command_prefix = "--", self_bot=True)

@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")




@bot.command()
async def bla(ctx):
    while True:
        await ctx.send("!d bump")
        time.sleep(8125)



bot.run(token, bot = False)