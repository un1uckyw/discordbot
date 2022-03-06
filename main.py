import discord
import logging
from discord.ext import commands
import os
import random

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command(name='changenick')
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    await member.edit(mute = True)

@bot.command(name = 'unmute')
async def unmute(ctx, member: discord.Member):
    await member.edit(mute = False)

@bot.command(name = 'ban')
async def ban(ctx, member: discord.Member):
    await member.ban()

@bot.command(name = 'kick')
async def kick(ctx, member: discord.Member):
    await member.kick()

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(807287859111002186)
    message = 'Ein mieses Gerät ist erschienen, {}!'
    await channel.send(message.format(member.mention))

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#
#    if message.content.startswith('$play'):
#        quotenumber = random.randint(1,5)
#        if quotenumber == 1:
#            await message.channel.send('Tokio kann man essen, ja, lecker!')
#        elif quotenumber == 2:
#            await message.channel.send('Sex ist wie Valorant Skins!')
#        elif quotenumber == 3:
#            await message.channel.send('Ich liebe es Kinder zu f-!')
#        elif quotenumber == 4:
#            await message.channel.send('Vallah meine Freundin ist so hässlich, ich mach jetzt Schluss mit sie!')
#        elif quotenumber == 5:
#            await message.channel.send('Zu Nunos Haus, große Haus, AEZ!')

bot.run('ODg4MTcxNzA1ODQxOTA5ODEy.YUO0XA.LxMXxEf0IPqp_zLV7hEflm35gcQ')
