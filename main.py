import discord, subprocess, sys, time, os, colorama, ctypes, json, requests, random, pytz
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from sys import argv
from colorama import Fore
from discord.ext import commands

def clear():
    os.system('cls')

def startup():
    print(f'{Fore.RED}d')
clear()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


token = input(f'{Fore.BLUE}enter {Fore.CYAN}auth token: {Fore.WHITE}')
purgemessage = input(f'{Fore.BLUE}enter {Fore.CYAN}the command: {Fore.WHITE}')


class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge_server"):
            channels=message.channel.guild.channels
        elif(message.content==purgemessage):
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(f'{Fore.BLUE}purging in:{Fore.CYAN} {channel}')
            try:
                async for mss in channel.history(limit=None):

                    if(mss.author==self.user):
                        print(f'{Fore.CYAN}message {Fore.CYAN}deleted {Fore.BLUE}-> {Fore.CYAN}{mss.content}')
                        try:
                            await mss.delete()
                        except:
                            print("couldn't delete a message")
            except:
                print("Can't read history!\n")

def start():
    print(f'''
{Fore.WHITE} cerberus purger by yy

 send the command [{Fore.CYAN}{purgemessage}{Fore.BLUE}] to delete junk (all messages in the selected will be deleted)
''')
os.system(f'title cerberus purger - yy')
clear()
start()

bot=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
bot.run(token, bot=False)

