#########################################################
#							#
#		© Copyright 2020 Anon0x19		#
#		All rights reserved			#
#		Author: anon0x19			#
#		Date: 09/05/2020			#
#							#
#########################################################

import requests
import discord
import asyncio
import json
from tabulate import tabulate
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Webhook, RequestsWebhookAdapter, File

TOKEN = "{your_api_key}"
client = commands.Bot(command_prefix = ".")

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
	if message.author == client.user:
		return
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
		if "error" in player:
			arr3.append("")
			arr3.append("Nicked Player?")
			arr2.append(arr3)
		else:
			bwLevel = str(player['stats']['BedWars']['level'])
			FKDR = player['stats']['BedWars']['final_k_d']
			WR = player['stats']['BedWars']['w_l']
			WS = player['stats']['BedWars']['winstreak']
			BBLR = player['stats']['BedWars']['bed_ratio']
			arr3.append(bwLevel + "✫")
			arr3.append(p)
			arr3.append(FKDR)
			arr3.append(WR)
			arr3.append(WS)
			arr3.append(BBLR)
			arr2.append(arr3)
			
	print(tabulate(arr2))
	await message.channel.send(">>> __**Bedwars Stats Bot**__" + "\n" + "\n" + "\n" + "Overall Stats:" + "\n" + "```" + "\n" + tabulate(arr2) + "\n" + "```" + "\n" + "`Made by Anon0x19#6246`")
	return arr2

client.run(TOKEN)
