#################################################
#												#
#			Copyright 2020 Anon0x19				#
#			All rights reserved					#
#			Author: anon0x19					#
#			Date: 09/05/2020					#
#												#
#################################################

import requests
import discord
import asyncio
import json
from tabulate import tabulate
from discord.ext import commands
from discord.ext.commands import Bot
from discord import RequestsWebhookAdapter, File
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

TOKEN = "NzA4Mzg5ODY1OTQyOTQxNjk2.XrWsSA.SFpCLC9jXngDNwo_v-uBslORQkg"
#webhook = DiscordWebhooks("https://discordapp.com/api/webhooks/708452057593544734/qnAFjGrojGXdla0Xz3HiyGMEaXsD2RiUNnwc6tVJmrADQlFuPULSUm-oHSOFiiG_E0Ct")
client = commands.Bot(command_prefix=".")
channel_ids = ["708405698110816368", "708452116573847662"]

arr1 = []
x = ""
hh = []
mm = []
ss = []
arr2 = ["Level", "Username", "FKDR", "WR", "WS", "BBLR"]
arr3 = []
COLOUR = "blue"
n = 0


@client.event
async def on_ready():
    print("Bot is running")
    for i in range(1, 24):
        hh.append(i)
    for i in range(1, 60):
        mm.append(i)
        ss.append(i)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        arr1 = []
        arr2 = [["LV", "Username", "FKDR", "WR", "WS", "BBLR"]]
        arr3 = []
        content = message.content

        if ".overall" in content:
            arr1.append(content.replace(".overall ", ""))
            Type = "Overall"
        elif "." not in content:
            Type = "Overall"
            arr1 = content.split(", ")
            for i in arr1:
                for j in hh:
                    for k in mm:
                        for l in ss:
                            time = "[" + str(j) + ":" + str(k) + ":" + str(l) + "]"
                            if time in i:
                                arr1[arr1.index(i)] = arr1[arr1.index(i)].replace(
                                    time + " [Client thread/INFO]: [CHAT] ONLINE: ", "")
            for p in arr1:
                arr3 = []
                player = requests.get("https://api.slothpixel.me/api/players/" + p).json()
                data = requests.get("https://api.hypixel.net/player?key=c47d4ab6-ada5-4378-86bd-9ff8fa78fd51&name=" + p).json()
                if len(arr1) == 1:
                    if len(p) < 2:
                        embed3 = discord.Embed(
                        title="Bedwars Stats Bot",
                        colour = discord.Colour(0x000000)
                        )
                        pl = "might be Nicked"
                        arr3.append("")
                        arr3.append(str(p) + "might be Nicked")
                        arr2.append(arr3)
                        embed3.add_field(name = "Player Name: ", value = p, inline = True)
                        embed3.add_field(name = "Info: ", value = "Player is either using a nick or does not exist.", inline = True)
                        embed3.set_footer(text="Made by Anon0x19#6246")
                        await message.channel.send(embed=embed3)

                    else:
                        if "error" in player:
                            embed3 = discord.Embed(
                            title="Bedwars Stats Bot",
                            colour = discord.Colour(0x000000)
                            )
                            pl = "might be Nicked"
                            arr3.append("")
                            arr3.append(str(p) + "might be Nicked")
                            arr2.append(arr3)
                            embed3.add_field(name = "Player Name: ", value = p, inline = True)
                            embed3.add_field(name = "Info: ", value = "Player is either using a nick or does not exist.", inline = True)
                            embed3.set_footer(text="Made by Anon0x19#6246")
                            await message.channel.send(embed=embed3)

                        elif data['player']['lastLogin'] > data['player']['lastLogout']:
                            embed1 = discord.Embed(
                            title="Bedwars Stats Bot",
                            colour = discord.Colour.green()
                            )
                            pl = p
                            bwLevel1 = str(player['stats']['BedWars']['level'])
                            bwLevel = bwLevel1 + "✫"
                            FKDR = player['stats']['BedWars']['final_k_d']
                            WR = player['stats']['BedWars']['w_l']
                            WS = player['stats']['BedWars']['winstreak']
                            BBLR = player['stats']['BedWars']['bed_ratio']
                            arr3.append(bwLevel)
                            arr3.append(p)
                            arr3.append(FKDR)
                            arr3.append(WR)
                            arr3.append(WS)
                            arr3.append(BBLR)
                            arr2.append(arr3)

                            embed1.add_field(name = "Player Name: ", value = pl, inline = False)
                            embed1.add_field(name = "Bedwars Level: ", value = bwLevel, inline = False)
                            embed1.add_field(name = "FKDR: ", value = FKDR, inline = False)
                            embed1.add_field(name = "WR: ", value = WR, inline = False)
                            embed1.add_field(name = "WS: ", value = WS, inline = False)
                            embed1.add_field(name = "BBLR: ", value = BBLR, inline = False)
                            embed1.set_footer(text="Made by Anon0x19#6246")
                            await message.channel.send(embed=embed1)

                        elif data['player']['lastLogin'] < data['player']['lastLogout']:
                            embed2 = discord.Embed(
                            title="Bedwars Stats Bot",
                            colour = discord.Colour.red()
                            )
                            if len(arr1) == 1:
                                pl = p
                                bwLevel1 = str(player['stats']['BedWars']['level'])
                                bwLevel = bwLevel1 + "✫"
                                FKDR = player['stats']['BedWars']['final_k_d']
                                WR = player['stats']['BedWars']['w_l']
                                WS = player['stats']['BedWars']['winstreak']
                                BBLR = player['stats']['BedWars']['bed_ratio']
                                arr3.append(bwLevel)
                                arr3.append(p)
                                arr3.append(FKDR)
                                arr3.append(WR)
                                arr3.append(WS)
                                arr3.append(BBLR)
                                arr2.append(arr3)

                                embed2.add_field(name = "Player Name: ", value = pl, inline = False)
                                embed2.add_field(name = "Bedwars Level: ", value = bwLevel, inline = False)
                                embed2.add_field(name = "FKDR: ", value = FKDR, inline = False)
                                embed2.add_field(name = "WR: ", value = WR, inline = False)
                                embed2.add_field(name = "WS: ", value = WS, inline = False)
                                embed2.add_field(name = "BBLR: ", value = BBLR, inline = False)
                                embed2.set_footer(text="Made by Anon0x19#6246")
                                await message.channel.send(embed=embed2)



            if len(arr1) > 1:
                for a in arr1:
                    arr3 = []
                    player = requests.get("https://api.slothpixel.me/api/players/" + a).json()
                    data = requests.get("https://api.hypixel.net/player?key=c47d4ab6-ada5-4378-86bd-9ff8fa78fd51&name=" + a).json()
                    if "error" in player:
                        pl = "might be Nicked"
                        arr3.append("")
                        arr3.append(str(a) + "might be Nicked")
                        arr2.append(arr3)
                    else:
                        embed4 = discord.Embed(
                        title="Bedwars Stats Bot",
                        colour = discord.Colour.blue()
                        )
                        pl = a
                        bwLevel1 = str(player['stats']['BedWars']['level'])
                        bwLevel = bwLevel1 + "✫"
                        FKDR = player['stats']['BedWars']['final_k_d']
                        WR = player['stats']['BedWars']['w_l']
                        WS = player['stats']['BedWars']['winstreak']
                        BBLR = player['stats']['BedWars']['bed_ratio']
                        arr3.append(bwLevel)
                        arr3.append(a)
                        arr3.append(FKDR)
                        arr3.append(WR)
                        arr3.append(WS)
                        arr3.append(BBLR)
                        arr2.append(arr3)

                embed4.add_field(name = "Overall Stats ", value = "```" + tabulate(arr2, tablefmt="plain") + "```", inline = True)
                embed4.set_footer(text="Made by Anon0x19#6246")
                await message.channel.send(embed=embed4)
            id = client.get_guild(673662940133720064)
            print(tabulate(arr2))
    #webhook.set_content(content="__**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
    # channel = client.get_channel(708405698110816368)
    # await message.author.send("```" + "\n" + "Overall Stats:" + "\n" + tabulate(arr2) + "\n" + "```")
    # await message.channel.send(">>> __**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
    #webhook.send()
    # return arr2





# async def test(author, message):
# await message.author.send(arr2)
# await client.delete_message(message)

# Webhook.send("Hello Thots, this is a test", username="Bedwars Stats")
client.run(TOKEN)
