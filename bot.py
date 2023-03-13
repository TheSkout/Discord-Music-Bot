# Setup
import discord
import ffmpeg
import yt_dlp
from yt_dlp import YoutubeDL
from discord import FFmpegPCMAudio
from config import settings
from discord.ext import commands
from discord.utils import get
prefix = settings['PREFIX']
client = commands.Bot(command_prefix = commands.when_mentioned_or(settings['PREFIX']), intents=discord.Intents.all())
client.remove_command('help') 
# Setup End

# Startup
@client.event
async def on_ready():
	print(f"Logged on as {settings['NAME BOT']}")
	print("Created by TheSkout#8213 (Discord)")
# Startup End


@client.command(pass_context = True) # join command
async def join(ctx):
    if (ctx.author.voice):
        vchan = ctx.message.author.voice.channel
        await vchan.connect()
        await ctx.reply("Successfully connected to voice channel")
    else:
        await ctx.reply("You must be in voice channel to run this command")

@client.command(pass_context = True) # leave command
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.reply("Successfully disconnected from the voice channel")
    else:
        await ctx.reply("Im not in the voice channel")


@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.reply('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.reply("Bot is already playing")
        return


# command to resume voice if it is paused
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.reply('Bot is resuming')


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.reply('Bot has been paused')


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.reply('Stopping...')






client.run(settings['TOKEN']) # you can paste your token in config.py file, as well as other settings
# If you need any help with, you can open issue on GitHub, or you can DM me in Discord: TheSkout#8213