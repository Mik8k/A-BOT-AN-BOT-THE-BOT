import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def play(ctx, url):
    if ctx.author.voice is None:
        await ctx.send("Você precisa estar em um canal de voz!")
        return

    channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        await channel.connect()
    elif ctx.voice_client.channel != channel:
        await ctx.voice_client.move_to(channel)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    source = await discord.FFmpegOpusAudio.from_probe(audio_url)
    ctx.voice_client.play(source)
    await ctx.send(f"Tocando: {info['title']}")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

bot.run('put you bot token')
