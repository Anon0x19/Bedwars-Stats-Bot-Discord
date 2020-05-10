#####################################################
#													#
#			© Copyright 2020 Anon0x19				#
#				All rights reserved					#
#				Author: anon0x19					#
#				Date: 09/05/2020					#
#													#
#####################################################

import requests
import discord
import asyncio
from tabulate import tabulate
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Webhook, RequestsWebhookAdapter, File

TOKEN = "NzA4Mzg5ODY1OTQyOTQxNjk2.XrWsSA.SFpCLC9jXngDNwo_v-uBslORQkg"
#webhook = Webhook.partial(708452057593544734, "qnAFjGrojGXdla0Xz3HiyGMEaXsD2RiUNnwc6tVJmrADQlFuPULSUm-oHSOFiiG_E0Ct", adapter=RequestsWebhookAdapter())
client = commands.Bot(command_prefix = ".")
channel_ids = ["708405698110816368", "708452116573847662"]

arr1 = []
x = ""
hh = []  
mm = [] 
ss = []
arr2 = ["LV", "Username", "FKDR", "WR", "WS", "BBLR"]
arr3 = []
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
	arr2 = [["LV", "Username", "FKDR", "WR", "WS", "BBLR"]]
	arr3 = []
	content = message.content
	arr1 = content.split(", ")
	for i in arr1:
		for j in hh:
			for k in mm:
				for l in ss:
					time = "[" + str(j) + ":" + str(k) + ":" + str(l) + "]"
					if time in i:
						arr1[arr1.index(i)] = arr1[arr1.index(i)].replace(time + " [Client thread/INFO]: [CHAT] ONLINE: ", "")
	print(arr1)
	for p in arr1:
		arr3 = []
		player = requests.get("https://api.slothpixel.me/api/players/" + p).json()

		def getInfo(json, param):
 			try:
 				return int(json['achievements']['bedwars_level'])
 				return int(json['stats']['Bedwars'][param])
 			except:
 				return 0

		bwLevel1 = player['stats']['BedWars']['level']
		bwLevel = str(bwLevel1) +"✫"
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
	print(arr2)

	id = client.get_guild(673662940133720064)
	print(tabulate(arr2))
	#channel = client.get_channel(708405698110816368)
	#await message.author.send("```" + "\n" + "Overall Stats:" + "\n" + tabulate(arr2) + "\n" + "```")
	await message.channel.send(">>> __**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
	#async def test(author, message):
	#await message.author.send(arr2)
	#await client.delete_message(message)

#Webhook.send("Hello Thots, this is a test", username="Bedwars Stats")
client.run(TOKEN)
