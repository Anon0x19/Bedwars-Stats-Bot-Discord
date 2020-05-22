# Bedwars Stats Discord Bot

Bedwars Stats Bot for discord programmed in python 3.7.5

## To get it workingon your server
* GitClone the repository or download StatsBot1
* Change {TOKEN} with your bots token and save the file.
* Change {API_KEY} with your Hypixel API key (You can obtain this by logging in and doing /api new and then copying and pasting it).
* Install all the modules (Using pip install)

And its ready to be used!

Note: requirements.txt and Procfile have been already been done. So the bot is ready to be hosted from a server.

## How to use the check stats for all player feature:

* MacOS/Unix/Linux:
  * Badlion Client: `<tail -f "./Library/Application Support/minecraft/logs/blclient/minecraft/latest.log" | grep "ONLINE:">`
  * Vanilla/Forge: `<tail -f "./Library/Application Support/minecraft/logs/latest.log" | grep "ONLINE:">`
* Windows:
  * Badlion Client: `<Get-Content "$env:APPDATA\.minecraft\logs\blclient\minecraft\latest.log" -Wait | where { $_ -match "Online:"}>`
  * Vanilla/Forge: `<Get-Content "$env:APPDATA\.minecraft\logs\latest.log" -Wait | where { $_ -match "Online:"}>`
  * Lunar Client: `<Get-Content "$env:APPDATA\lunarclient\logs\latest.log" -Wait | where { $_ -match "Online:"}>`

Note: For MacOS the code will have to be executed on terminal and for windows you will have to execute it through powershell although you can open notepad, copy paste it and save the file as (name).ps1 and then you can just open that file.
You will have to copy the the output form start to finish so that includes `<[time] [Client thread/INFO]: [CHAT] ONLINE:>` and all the players.


### Credits: 
- MinuteBrain (No GitHub page as of right now, Discord: BoomZa#5926)
- [Need_Not](https://github.com/NeedNot)
