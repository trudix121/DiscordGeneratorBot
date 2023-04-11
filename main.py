import numpy
import os
import discord
from dotenv import load_dotenv
from config import cooldown
from config import channel
from discord import *
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
color = 'F80E06'
Embed2 = Embed(title='Failed')
Embed1 = Embed(title="Succes")
Embed3 = Embed(title="Succes")
load_dotenv()
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
#client = app_commands.Commandclient(client)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        Embed2.add_field(name='', value=(f'esti in cooldown! Cooldown: 1 minut'), inline=False)
        await ctx.send(embed=Embed2)

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command(name='gen')
@commands.cooldown(1, cooldown, type=commands.BucketType.user)
async def ping(ctx, stock:str):
    if ctx.channel.id == 1094672677521854546:
      try:
       with open(f'./stock/{stock}.txt') as fg:
        first_line = fg.readlines()
        random_line = numpy.random.choice(first_line)
        Embed1.add_field(name='', value=f'Te rog verifica ti dm-urile , in caz ca nu primesti nimic in dm , inseamna ca ai dm urile inchise!', inline=False)
        Embed3.add_field(name="Account:", value=f"```{random_line}```",)
        await ctx.author.send()
        await ctx.send(embed=Embed1)

      except FileNotFoundError:
         Embed2.add_field(name='', value=f'Contul specificat de tine nu a fost gasit in baza mea de date!', inline=False)
         await ctx.send(embed=Embed2)
    else:
        Embed2.add_field(name='', value=f'Canalul in care vrei tu sa generezi un cont este gresit!', inline=False)
        await ctx.send(embed=Embed2)


@client.command(name='test', description="test", guild=discord.Object(id=1091843276061028383))
async def x(interaction):
    await interaction.response.send_message('test')



@client.command()
async def stock(ctx):
    folder_path = './stock'
    embed = Embed(title="Stock ul valabil")
    for file_name in os.listdir(folder_path):
        name, extension = os.path.splitext(file_name)
        if not extension:
            print(file_name)
        file_path2 = os.path.join(folder_path, file_name)
        with open(file_path2, 'r') as f:
            lines = f.readlines()
            embed.add_field(name='', value=f'{name} : {len(lines)} conturi', inline=False)
    await ctx.send(embed=embed)


'''@client.command()
async def stock(ctx):
 folder_path = './stock'
 for file_name in os.listdir(folder_path):
    split_text = os.path.splitext(file_name)
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        await ctx.send(f'{split_text}: {len(lines)} conturi')'''
client.run(os.environ.get('TOKEN'))


#ctx.send(f'{stock}')

