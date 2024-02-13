import requests
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='c!', intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync()
  print(f"Logged In As {bot.user}")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Key Links | Made By Leafy"))

@discord.app_commands.checks.cooldown(1, 10)
@bot.tree.command(name="fluxus-key", description="Get Fluxus Key")
async def fluxus(interaction, link: str):
    try:
        data = {"link": link}
        r = requests.post("https://glowworm-adapting-manatee.ngrok-free.app/fluxus/", json=data)
        message = r["message"]
        em = discord.Embed(color=0x76b6ef)
        em.add_field(name="Fluxus Key Bypass", value=f"{message}")
        em.set_footer(text='Made By Leafy | Come Back Next Time')
        await interaction.response.send_message("__Copy Your Key__", embed=em)
    except:
        await interaction.response.send_message("```kindly check your provided link again. There was an error.```")

@fluxus.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)

bot.run("MTIwNjI2Nzc0OTQ2NzI5MTcwOQ.GVkQ5M.HNi3kyiDOcHSoNKzDnle5H8TafAscIcTY979dA")