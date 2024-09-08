import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

load_dotenv()

#tests

@bot.event
async def on_ready():
    print("iekurbulejos")

@bot.command()
async def zerg(ctx):
    allowed_mentions = discord.AllowedMentions(everyone = True)
    await ctx.send(content = "@everyone MUMS VAJAG ZERG", allowed_mentions = allowed_mentions)

@bot.command()
async def zirgs(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278468639363956787/zirgs.gif?ex=66d435f4&is=66d2e474&hm=8b08f4630657c72fd7672c09e99d0ce3c29ed9dcc25c27428144e5bd406db574&")

@bot.command()
async def baze(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278468119588769792/imagebaze.png?ex=66d43578&is=66d2e3f8&hm=c87dbe715c298f693db474cf676e55e777eb453331a6c7611ddbf85d8d55532e&")

@bot.command()
async def dzert(ctx):
    await ctx.send(content="Alkohola lietošanai ir negatīva ietekme. Alkoholisko dzērienu pārdošana, iegādāšanās un nodošana nepilngadīgām personām ir aizliegta")

@bot.command()
async def curb(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278468214808121384/curb.gif?ex=66d4358f&is=66d2e40f&hm=188f5bdc8eb7783fd10e4d223d9e5a513061c43df29dcddf56207b4f01a02b4f&")

@bot.command()
async def seks(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278468907916726343/gamer-1.gif?ex=66d43634&is=66d2e4b4&hm=447f596b97b123e207b7060e245961dca3aef43d697c3593b12bf3f45180a21b&")


@bot.command()
async def laiks(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278469200297328744/watch.gif?ex=66d4367a&is=66d2e4fa&hm=9e1212d020c9bfd5c3fa7e3686eba10a03028085b7d1ac466a7a985c3899bb80&")


@bot.command()
async def nezvers(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278469385836564576/dusma.gif?ex=66d436a6&is=66d2e526&hm=c063e022565fa1bdcda78e6229af50d180e564f8df1d2b2e25c1c86fb1885013&")

@bot.command()
async def pankukas(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278469889786511512/pankukas.gif?ex=66d4371e&is=66d2e59e&hm=127c62a789accaf430cfa6ab154f8cea977869e0b5b1d87d8966eeb66e8c1b15&")

@bot.command()
async def putns(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1278470031205863484/putns.gif?ex=66d43740&is=66d2e5c0&hm=3e2f0d617511308e97b64a3f2880d8979c585b4a7bb92d92d10249a88df996e7&")

@bot.command()
async def fleksis(ctx):
    await ctx.send(content="https://media.discordapp.net/attachments/1125102760568823868/1126082049808285777/ezgif-3-614a7e22eb.gif?ex=66d433a2&is=66d2e222&hm=9eb7c11ac0dfd1de12a522511bc0d37e5e5d6172f9a2ff64be32e45ccda55f15&")

@bot.command()
async def sokolade(ctx):
    await ctx.send(content="https://media.discordapp.net/attachments/974387289193078877/977762987983134720/cachedGif.gif?ex=66df08fe&is=66ddb77e&hm=a53e7a0bedc9f60db37ac7869107fcdd18af6ce0b74db30fa8db6d25349fbe5a&")

@bot.command()
async def klips(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1265395908942757986/1282432125664235621/410d163e9e5941c3b925036cbc8544f6.MP4?ex=66df557d&is=66de03fd&hm=e452df6400bf8ef1b66d2833b1c34203fe739ebc06511b9f178d4c225291c6fa&")


bot.run(os.environ['TOKEN'])
