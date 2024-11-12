import requests
import discord
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents)




def quote(query):
    if query == 'random':
        response = requests.get('https://zenquotes.io/api/random')
        json_data = json.loads(response.text)
        #quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
        quote = f"**{json_data[0]['q']}**\n\n*— {json_data[0]['a']}*"
        return quote
    
    elif query == 'stoic2':
         response = requests.get('https://stoic.tekloon.net/stoic-quote')
         json_data = json.loads(response.text)
         #quote = json_data['data']['quote'] + "\r\n - " + json_data['data']['author']
         quote = f"**{json_data['data']['quote']}**\n\n*— {json_data['data']['author']}*"

         return quote
    

    elif query == 'stoic':
         with open('stoic_quotes.json', 'r') as f:
             json_data = json.load(f)
         quote_data = random.choice(json_data['quotes'])
    
         # Format the quote and author
         quote = f"**{quote_data['text']}**\n*{quote_data['author']}*"
         



         return quote



    elif query == 'programming':
         with open('programming_quotes.json','r') as f:
            json_data = json.load(f)
         random_quote = random.choice(json_data)
         #quote = random_quote['en'] + "\r\n - " + random_quote['author']
         quote = f"**{random_quote['en']}**\n\n*— {random_quote['author']}*"

         return quote
    
    elif query in ['suntzu', 'sun tzu','Sun Tzu']:
         with open('suntzu_quotes.json','r') as f:
            json_data = json.load(f)
         #quote = random.choice(json_data) + '\r\n-' 'Sun Tzu'
         quote = f"**{random.choice(json_data)}**\n\n*— Sun Tzu*"
         return quote
    
    elif query in ['topg']:
        with open('topg.json','r') as f:
            json_data = json.load(f)
        quote = f"**{random.choice(json_data)}**\n\n*— Andrew Tate*"
        return quote
    elif query in ['stallman']:
        with open('stallman.json','r') as f:
            json_data = json.load(f)
        quote = f"**{random.choice(json_data)}**\n\n*— Richard Stallman*"
         
        





@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')




@bot.command()
async def pand(ctx, query: str):
    
    await ctx.send(quote(query))




@bot.command(help="Listi az pand haye mojood")
async def help(ctx, query: str):
    help_messages = """
    **Pand haye mojood:**
    - 'random': - In ke maloome chie khob ahmaq
    - 'stoic': - Stoic pands
    - 'stoic2': - Stoic pands from another source
    - 'programming': - Programming pands
    - 'suntzu': - Sun Tzu pands
    - 'topg': - Andrew Tate pands
    - 'stallman': - Richard Stallman pands

    """
    await ctx.send(help_messages)



#with open('config.json','r') as f:
 #    config = json.load(f)


TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("Error: DISCORD_TOKEN environment variable not set.")
else:
   
    bot.run(TOKEN)



#TOKEN = config['TOKEN']

#if TOKEN is None:
   # print("Error: DISCORD_TOKEN environment variable not set.")
#else:
   
   # bot.run(TOKEN)

    



