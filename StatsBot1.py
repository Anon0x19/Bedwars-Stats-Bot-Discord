#################################################
#                                               #
#           Copyright 2020 Anon0x19             #
#           All rights reserved                 #
#           Author: Anon0x19                    #
#           Date: 09/05/2020                    #
#                                               #
#################################################
import requests
#import base64
#from PIL import Image
import discord
import asyncio
import json
from tabulate import tabulate
from discord.ext import commands, tasks
from discord.ext.commands import Bot, MemberConverter
from discord import RequestsWebhookAdapter, File, Webhook, AsyncWebhookAdapter
import aiohttp
from discord.utils import get

TOKEN = {TOKEN}
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
ver = [" ", ",", "-", ";", ":", "ç", "ñ", ",", "´", "`", "„", "…", "–", "¨", "*", "^", "{", "}", "[", "]", "¿", "¡", "'", "?", "=", ")", "(", "/", "&", "%", "$", "·", "!", "ª", "º", "@", "#", "<" ">"]
emoji = "\N{THUMBS UP SIGN}"

#tasks.loop(seconds=15.0)
#async def change_nick():



#name_change.before_loop(client.wait_until_ready())
#name_change.start()


@client.event
async def on_ready():
    print("Bot is running")
    for i in range(1, 24):
        hh.append(i)
    for i in range(1, 60):
        mm.append(i)
        ss.append(i)

#async def my_background_task():
#    await client.wait_until_ready()


@client.event
async def on_message(message):
    channel = discord.utils.get(message.guild.channels, name="bwstats")
    if message.author == client.user:
        return

    else:
        if message.channel == channel:
            arr1 = []
            arr2 = [["LV", "Username", "FKDR", "WR", "WS", "BBLR"]]
            arr3 = []
            content = message.content
            await message.add_reaction(emoji)
            if ".overall" in content:
                arr1.append(content.replace(".overall ", ""))
                Type = "Overall"
                for pla in arr1:
                    #uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(pla)).json()['id']
                    #url = json.loads(base64.b64decode(requests.get('https://sessionserver.mojang.com/session/minecraft/profile/{}'.format(uuid)).json()['properties'][0]['value'])
                    #     .decode('utf-8'))['textures']['SKIN']['url']
                    arr3 = []
                    player = requests.get("https://api.slothpixel.me/api/players/" + pla).json()
                    data = requests.get("https://api.hypixel.net/player?key=c47d4ab6-ada5-4378-86bd-9ff8fa78fd51&name=" + pla).json()
                    if "error" in player:
                        embed5 = discord.Embed(
                        title="Bedwars Stats Bot",
                        colour = discord.Colour(0x000000)
                        )
                        pl = "might be Nicked"
                        arr3.append("")
                        arr3.append(str(pla) + "might be Nicked")
                        arr2.append(arr3)
                        embed5.add_field(name = "Player Name: ", value = pla, inline = True)
                        embed5.add_field(name = "Info: ", value = "Player is either using a nick or does not exist.", inline = True)
                        embed5.set_footer(text="Made by Anon0x19#6246")
                        await message.channel.send(channel, embed=embed5)

                    elif isinstance(data['player']['lastLogin'], int) == False or isinstance(player['last_logout'], int) == False:
                        embed6 = discord.Embed(
                        title="Bedwars Stats Bot",
                        description="Overall Stats",
                        colour = discord.Colour(0x000000)
                        )
                        pl = "might be Nicked"
                        arr3.append("")
                        arr3.append(str(pla))
                        arr2.append(arr3)
                        embed6.add_field(name = "Player Name: ", value = p, inline = True)
                        embed6.add_field(name = "Info: ", value = "Player has played hypixel in the past but has no data for Bedwars.", inline = True)
                        embed6.set_footer(text="Made by Anon0x19#6246")
                        await message.channel.send(channel, embed=embed6)

                    elif data['player']['lastLogin'] > data['player']['lastLogout']:
                        embed7 = discord.Embed(
                        title="Bedwars Stats Bot",
                        description="Overall Stats",
                        colour = discord.Colour.green()
                        )
                        bwLevel1 = str(player['stats']['BedWars']['level'])
                        bwLevel = bwLevel1 + "✫"
                        FKDR = player['stats']['BedWars']['final_k_d']
                        WR = player['stats']['BedWars']['w_l']
                        WS = player['stats']['BedWars']['winstreak']
                        BBLR = player['stats']['BedWars']['bed_ratio']
                        IRON = player['stats']['BedWars']['resources_collected']['iron']
                        GOLD = player['stats']['BedWars']['resources_collected']['gold']
                        DIAMOND = player['stats']['BedWars']['resources_collected']['diamond']
                        EMERALD = player['stats']['BedWars']['resources_collected']['emerald']
                        KDR = player['stats']['BedWars']['k_d']
                        coins = player['stats']['BedWars']['coins']
                        FK = player['stats']['BedWars']['final_kills']
                        FD = player['stats']['BedWars']['final_deaths']
                        KK = data['player']['stats']['Bedwars']['kills_bedwars'] + player['stats']['BedWars']['final_kills']
                        DD = player['stats']['BedWars']['deaths']
                        GP = player['stats']['BedWars']['games_played']
                        WINS = player['stats']['BedWars']['wins']
                        VD = player['stats']['BedWars']['void_deaths']

                        arr3.append(bwLevel)
                        arr3.append(pla)
                        arr3.append(FKDR)
                        arr3.append(WR)
                        arr3.append(WS)
                        arr3.append(BBLR)
                        arr2.append(arr3)

                        embed7.add_field(name = "Player Name: ", value = "`" + pla + "`", inline = False)

                        embed7.add_field(name = "Bedwars Level: ", value = bwLevel, inline = True)
                        embed7.add_field(name = "Total Coins: ", value = coins, inline = True)
                        embed7.add_field(name = "Games Played: ", value = GP, inline = True)

                        embed7.add_field(name = "WS: ", value = WS, inline = True)
                        embed7.add_field(name = "WR: ", value = WR, inline = True)
                        embed7.add_field(name = "BBLR: ", value = BBLR, inline = True)

                        embed7.add_field(name = "FKDR: ", value = FKDR, inline = True)
                        embed7.add_field(name = "Total Final Kills ", value = FK, inline = True)
                        embed7.add_field(name = "Total Final Deaths ", value = FD, inline = True)

                        embed7.add_field(name = "KDR ", value = KDR, inline = True)
                        embed7.add_field(name = "Total Kills ", value = KK, inline = True)
                        embed7.add_field(name = "Total Deaths ", value = DD, inline = True)

                        embed7.add_field(name = "Wins ", value = WINS, inline = True)
                        embed7.add_field(name = "Void Deaths ", value = VD, inline = True)

                        embed7.add_field(name = "Iron Collected: ", value = IRON, inline = True)

                        embed7.add_field(name = "Gold Collected: ", value = GOLD, inline = True)
                        embed7.add_field(name = "Diamonds Collected: ", value = DIAMOND, inline = True)
                        embed7.add_field(name = "Emeralds Collected: ", value = EMERALD, inline = True)
                        embed7.set_footer(text="Made by Anon0x19#6246")
                        embed7.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                        await message.channel.send(channel, embed=embed7)

                    elif data['player']['lastLogin'] < data['player']['lastLogout']:
                        embed8 = discord.Embed(
                        title="Bedwars Stats Bot",
                        description="Overall Stats",
                        colour = discord.Colour.red()
                        )
                        bwLevel1 = str(player['stats']['BedWars']['level'])
                        bwLevel = bwLevel1 + "✫"
                        FKDR = player['stats']['BedWars']['final_k_d']
                        WR = player['stats']['BedWars']['w_l']
                        WS = player['stats']['BedWars']['winstreak']
                        BBLR = player['stats']['BedWars']['bed_ratio']
                        IRON = player['stats']['BedWars']['resources_collected']['iron']
                        GOLD = player['stats']['BedWars']['resources_collected']['gold']
                        DIAMOND = player['stats']['BedWars']['resources_collected']['diamond']
                        EMERALD = player['stats']['BedWars']['resources_collected']['emerald']
                        KDR = player['stats']['BedWars']['k_d']
                        coins = player['stats']['BedWars']['coins']
                        FK = player['stats']['BedWars']['final_kills']
                        FD = player['stats']['BedWars']['final_deaths']
                        KK = data['player']['stats']['Bedwars']['kills_bedwars'] + player['stats']['BedWars']['final_kills']
                        DD = player['stats']['BedWars']['deaths']
                        GP = player['stats']['BedWars']['games_played']
                        WINS = player['stats']['BedWars']['wins']
                        VD = player['stats']['BedWars']['void_deaths']

                        arr3.append(bwLevel)
                        arr3.append(pla)
                        arr3.append(FKDR)
                        arr3.append(WR)
                        arr3.append(WS)
                        arr3.append(BBLR)
                        arr2.append(arr3)

                        embed8.add_field(name = "Player Name: ", value = "`" + pla + "`", inline = False)

                        embed8.add_field(name = "Bedwars Level: ", value = bwLevel, inline = True)
                        embed8.add_field(name = "Total Coins: ", value = coins, inline = True)
                        embed8.add_field(name = "Games Played: ", value = GP, inline = True)

                        embed8.add_field(name = "WS: ", value = WS, inline = True)
                        embed8.add_field(name = "WR: ", value = WR, inline = True)
                        embed8.add_field(name = "BBLR: ", value = BBLR, inline = True)

                        embed8.add_field(name = "FKDR: ", value = FKDR, inline = True)
                        embed8.add_field(name = "Total Final Kills ", value = FK, inline = True)
                        embed8.add_field(name = "Total Final Deaths ", value = FD, inline = True)

                        embed8.add_field(name = "KDR ", value = KDR, inline = True)
                        embed8.add_field(name = "Total Kills ", value = KK, inline = True)
                        embed8.add_field(name = "Total Deaths ", value = DD, inline = True)

                        embed8.add_field(name = "Wins ", value = WINS, inline = True)
                        embed8.add_field(name = "Void Deaths ", value = VD, inline = True)

                        embed8.add_field(name = "Iron Collected: ", value = IRON, inline = True)

                        embed8.add_field(name = "Gold Collected: ", value = GOLD, inline = True)
                        embed8.add_field(name = "Diamonds Collected: ", value = DIAMOND, inline = True)
                        embed8.add_field(name = "Emeralds Collected: ", value = EMERALD, inline = True)
                        embed8.set_footer(text="Made by Anon0x19#6246")
                        embed8.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                        await message.channel.send(channel, embed=embed8)

            
            elif len(content) > 1 and len(content) < 17:
                for item1 in ver:
                    if item1 in content:
                        return

                if "." not in content:
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
                                arr3.append(str(p) + " might be Nicked")
                                arr2.append(arr3)
                                embed3.add_field(name = "Player Name: ", value = "`" + p + "`", inline = True)
                                embed3.add_field(name = "Info: ", value = "Player is either using a nick or does not exist.", inline = True)
                                embed3.set_footer(text="Made by Anon0x19#6246")
                                await message.channel.send(channel, embed=embed3)

                            else:
                                if "error" in player:
                                    embed9 = discord.Embed(
                                    title="Bedwars Stats Bot",
                                    colour = discord.Colour(0x000000)
                                    )
                                    pl = "might be Nicked"
                                    arr3.append("")
                                    arr3.append(str(p) + "might be Nicked")
                                    arr2.append(arr3)
                                    embed9.add_field(name = "Player Name: ", value = "`" + p + "`", inline = True)
                                    embed9.add_field(name = "Info: ", value = "Player is either using a nick or does not exist.", inline = True)
                                    embed9.set_footer(text="Made by Anon0x19#6246")
                                    embed9.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                                    await message.channel.send(channel, embed=embed9)

                                elif isinstance(data['player']['lastLogin'], int) == False or isinstance(player['last_logout'], int) == False:
                                    embed3 = discord.Embed(
                                    title="Bedwars Stats Bot",
                                    colour = discord.Colour(0x000000)
                                    )
                                    pl = "might be Nicked"
                                    arr3.append("")
                                    arr3.append(str(p))
                                    arr2.append(arr3)
                                    embed3.add_field(name = "Player Name: ", value = "`" + p + "`", inline = True)
                                    embed3.add_field(name = "Info: ", value = "Player has played hypixel in the past but has no data for Bedwars.", inline = True)
                                    embed3.set_footer(text="Made by Anon0x19#6246")
                                    embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                                    await message.channel.send(channel, embed=embed3)


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

                                    embed1.add_field(name = "Player Name: ", value = "`" + pl + "`", inline = False)
                                    embed1.add_field(name = "Bedwars Level: ", value = bwLevel, inline = False)
                                    embed1.add_field(name = "FKDR: ", value = FKDR, inline = False)
                                    embed1.add_field(name = "WR: ", value = WR, inline = False)
                                    embed1.add_field(name = "WS: ", value = WS, inline = False)
                                    embed1.add_field(name = "BBLR: ", value = BBLR, inline = False)
                                    embed1.set_footer(text="Made by Anon0x19#6246")
                                    embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                                    await message.channel.send(channel, embed=embed1)

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

                                        embed2.add_field(name = "Player Name: ", value = "`" + pl + "`", inline = False)
                                        embed2.add_field(name = "Bedwars Level: ", value = bwLevel, inline = False)
                                        embed2.add_field(name = "FKDR: ", value = FKDR, inline = False)
                                        embed2.add_field(name = "WR: ", value = WR, inline = False)
                                        embed2.add_field(name = "WS: ", value = WS, inline = False)
                                        embed2.add_field(name = "BBLR: ", value = BBLR, inline = False)
                                        embed2.set_footer(text="Made by Anon0x19#6246")
                                        embed2.set_thumbnail(url='https://cdn.discordapp.com/attachments/708405698110816368/711922001329258609/0d8e0598-57cc-4646-a533-f64dce1aa8d6_.png')
                                        await message.channel.send(channel, embed=embed2)



            elif "[Client thread/INFO]" in content:
                if "." not in content:
                    Type = "Overall"
                    arr1 = content.split(", ")
                    for i in arr1:
                        for j in hh:
                            for k in mm:
                                for l in ss:
                                    time = "[" + str(j) + ":" + str(k) + ":" + str(l) + "]"
                                    if time in i:
                                        arr1[arr1.index(i)] = arr1[arr1.index(i)].replace(time + " [Client thread/INFO]: [CHAT] ONLINE: ", "")
                    for a in arr1:
                        arr3 = []
                        player = requests.get("https://api.slothpixel.me/api/players/" + a).json()
                        data = requests.get("https://api.hypixel.net/player?key=c47d4ab6-ada5-4378-86bd-9ff8fa78fd51&name=" + a).json()
                        if "error" in player:
                            pl = "might be Nicked"
                            arr3.append("")
                            arr3.append(str(a) + " Nick?")
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
                    await message.channel.send(channel, embed=embed4)
                    id = client.get_guild(673662940133720064)
                    print(tabulate(arr2))
        #webhook.set_content(content="__**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
        # channel = client.get_channel(708405698110816368)
        # await message.author.send("```" + "\n" + "Overall Stats:" + "\n" + tabulate(arr2) + "\n" + "```")
        # await message.channel.send(">>> __**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
        #webhook.send()
        # return arr2
            else:
                return


#        channel2 = discord.utils.get(message.guild.channels, name="verify")
#        elif message.channel == channel2:
#            if ".verify" in content:
#                arr1.append(content.replace(".verify ", ""))
#                for play in arr1:
#                    player = requests.get("https://api.slothpixel.me/api/players/" + play).json()
#                    data = requests.get("https://api.hypixel.net/player?key=c47d4ab6-ada5-4378-86bd-9ff8fa78fd51&name=" + play).json()
#                    print(data['player']['socialMedia']['links']['DISCORD'])
#                    if data['player']['socialMedia']['links']['DISCORD'] == message.author:
#                        user = message.author
#                        role = discord.utils.get(user.server.roles, name="verified")
#                        await client.add_roles(user, role)

#                    else:
#                        return



# async def test(author, message):
# await message.author.send(arr2)
# await client.delete_message(message)

# Webhook.send("Hello Thots, this is a test", username="Bedwars Stats")
client.run(TOKEN)

