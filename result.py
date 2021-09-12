import discord
import os
import asyncio
import requests
import json
from bs4 import BeautifulSoup

client = discord.Client()






@client.event
async def on_message(message):
    ## HTTP GET Request
    result = requests.get('http://ntry.com/data/json/games/powerball/result.json')
    ## HTML 소스 가져오기
    html = result.text
    soup = BeautifulSoup(html, 'html.parser')

    data = str(soup)
    parsed_data = json.loads(data)

    round = parsed_data['date_round']
    ball = parsed_data['ball']
    powoe = parsed_data['pow_ball_oe']
    powuo = parsed_data['pow_ball_unover']
    balladd = parsed_data['def_ball_sum']
    defoe = parsed_data['def_ball_oe']
    defuo = parsed_data['def_ball_unover']
    defsize = parsed_data['def_ball_size']

    if message.content.startswith('!파워볼'):
        embed = discord.Embed(title="동행복권 파워볼", color=0x62c1cc)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/884810987620958271/886560903913422898/img_inbok_logo1.png")
        embed.add_field(name="회차", value=round, inline=False)
        embed.add_field(name="파워볼 홀/짝", value=powoe, inline=False)
        embed.add_field(name="파워볼 언더/오버", value=powuo, inline=False)
        embed.add_field(name="일반볼 홀/짝", value=defoe, inline=False)
        embed.add_field(name="일반볼 언더/오버", value=defuo, inline=False)
        embed.add_field(name="일반볼 합", value=balladd, inline=False)
        embed.add_field(name="일반볼 대/중/소", value=defsize, inline=False)
        await message.channel.send(embed=embed)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
