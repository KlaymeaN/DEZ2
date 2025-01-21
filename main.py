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



def normalize_query(query):
    query = query.lower()
    query = query.replace(" ", "")
    return query


def quote(query):

    query = normalize_query(query)

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
         quote = f"**{quote_data['text']}**\n*{quote_data['author']}*"
         
         image_folder = 'images/stoic'
         valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]

         image_file = random.choice(valid_images)
         image_path = os.path.join(image_folder, image_file)

         embed = discord.Embed(
            title="🧘 Stoic Pand",
            description=f"\"{quote}\"",
            color=discord.Color.purple()
         )

         file = discord.File(image_path, filename=image_file)
         embed.set_image(url=f"attachment://{image_file}")
         return embed, file
             
         



    elif query == 'programming':
         with open('programming_quotes.json','r') as f:
            json_data = json.load(f)
         random_quote = random.choice(json_data)
         quote = f"**{random_quote['en']}**\n\n*— {random_quote['author']}*"
         
         image_folder = 'images/programming'
         valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]

         image_file = random.choice(valid_images)
         image_path = os.path.join(image_folder, image_file)

         embed = discord.Embed(
            title="💻 Programming Pand",
            description=f"\"{quote}\"",
            color=discord.Color.blue()
         )

         file = discord.File(image_path, filename=image_file)
         embed.set_image(url=f"attachment://{image_file}")
         return embed, file        
    

    elif query == 'suntzu':
         with open('suntzu_quotes.json','r') as f:
            json_data = json.load(f)
         #quote = random.choice(json_data) + '\r\n-' 'Sun Tzu'
         quote = f"**{random.choice(json_data)}**\n\n*— Sun Tzu*"
         
         image_folder = 'images/suntzu'
         valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]
    
         image_file = random.choice(valid_images)
         image_path = os.path.join(image_folder, image_file)

         embed = discord.Embed(
            title="📚 Sun Tzu Pand",
            description=f"\"{quote}\"",
            color=discord.Color.orange()
         )

         file = discord.File(image_path, filename=image_file)
         embed.set_image(url=f"attachment://{image_file}")
         return embed, file
         
    

    elif query == 'topg':
        with open('topg.json','r') as f:
            json_data = json.load(f)
        quote = f"**{random.choice(json_data)}**\n\n*— Andrew Tate*"
        
        image_folder = 'images/topg'
        valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]

        image_file = random.choice(valid_images)
        image_path = os.path.join(image_folder, image_file)

        embed = discord.Embed(
            title="🥋 Andrew Tate Pand",
            description=f"\"{quote}\"",
            color=discord.Color.red()
        )

        file = discord.File(image_path, filename=image_file)
        embed.set_image(url=f"attachment://{image_file}")
        return embed, file
    


    elif query == 'stallman':
        with open('stallman.json','r') as f:
            json_data = json.load(f)
        quote = f"**{random.choice(json_data)}**\n\n*— Richard Stallman*"

        image_folder = 'images/stallman'
        valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]

        image_file = random.choice(valid_images)
        image_path = os.path.join(image_folder, image_file)

        embed = discord.Embed(
            title="🐧 Richard Stallman Pand",
            description=f"\"{quote}\"",
            color=discord.Color.blue()
        )

        file = discord.File(image_path, filename=image_file)
        embed.set_image(url=f"attachment://{image_file}")
        return embed, file 
    
    elif query == 'mc':
        with open('mc.json','r') as f:
            json_data = json.load(f)
        quote = f"**{random.choice(json_data)}**\n\n*— Minecraft*"
        #return quote
        image_folder = 'images/mc'
        valid_images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpeg', '.jpg'))]

        image_file = random.choice(valid_images)
        image_path = os.path.join(image_folder, image_file)

        embed = discord.Embed(
            title="💬 Minecraft Pand",
            description=f"\"{quote}\"",
            color=discord.Color.green()
        )
        #embed.set_footer(text="— Minecraft 🧊")

        file = discord.File(image_path, filename=image_file)
        embed.set_image(url=f"attachment://{image_file}")
        
        return embed, file



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



@bot.command()
async def pand(ctx, query: str):
    
    response = quote(query)
    
    if isinstance(response, tuple):
        embed, file = response
        await ctx.send(embed=embed, file=file)
    
    elif isinstance(response, str):
        await ctx.send(response)

    else:
        await ctx.send("Bebakshid, chi?")




@bot.command()
async def komak(ctx):
    help_messages = """
    **Pand haye mojood:**
    - 'random': - In ke maloome chie khob ahmaq
    - 'stoic': - Stoic pands
    - 'stoic2': - Stoic pands from another source
    - 'programming': - Programming pands
    - 'suntzu': - Sun Tzu pands
    - 'topg': - Andrew Tate pands
    - 'stallman': - Richard Stallman pands
    - 'mc': - Minecraft pands

    """
    await ctx.send(help_messages)




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

    



