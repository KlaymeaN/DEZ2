import requests
import discord
from discord.ext import commands
import json
import random


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents)




def quote(query):
    if query == 'random':
        response = requests.get('https://zenquotes.io/api/random')
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
        return quote
    elif query == 'stoic':
         response = requests.get('https://stoic.tekloon.net/stoic-quote')
         json_data = json.loads(response.text)
         quote = json_data['data']['quote'] + "\r\n - " + json_data['data']['author']
         return quote
    elif query == 'programming':
         with open('programming_quotes.json','r') as f:
            json_data = json.load(f)
         random_quote = random.choice(json_data)
         quote = random_quote['en'] + "\r\n - " + random_quote['author']
         return quote
        





@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')




@bot.command()
async def pand(ctx, query: str):
    
    await ctx.send(quote(query))

    

with open('config.json','r') as f:
     config = json.load(f)
TOKEN = config['TOKEN']

if TOKEN is None:
    print("Error: DISCORD_TOKEN environment variable not set.")
else:
   
    bot.run(TOKEN)

    



