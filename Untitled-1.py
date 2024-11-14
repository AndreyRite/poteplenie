import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",  intents=intents)


@bot.command(name="привет")
async def greet(ctx):
    await ctx.send(f"Привет, {ctx.author.name}! ")



@bot.command(name="помощь")
async def help_command(ctx):
    commands_list = (
        "!привет — бот поприветствует тебя\n"
        "!помощь — показать все доступные команды\n"
        "причина_(1-5)\n"
        "последствие_(1-5)"
    )
    await ctx.send(commands_list)

# Причины
@bot.command(name="причина_1")
async def cause_1(ctx):
    await ctx.send("Основной причиной глобального потепления является сжигание ископаемого топлива (нефть, уголь, газ), которое выделяет углекислый газ в атмосферу.")

@bot.command(name="причина_2")
async def cause_2(ctx):
    await ctx.send("Дефорестация — вырубка лесов — уменьшает количество деревьев, поглощающих CO2, что усиливает парниковый эффект.")

@bot.command(name="причина_3")
async def cause_3(ctx):
    await ctx.send("Сельское хозяйство, особенно животноводство, приводит к выбросам метана, который является мощным парниковым газом.")

@bot.command(name="причина_4")
async def cause_4(ctx):
    await ctx.send("Индустриальные процессы и производство, такие как цемент и металлургия, выбрасывают значительное количество парниковых газов.")

@bot.command(name="причина_5")
async def cause_5(ctx):
    await ctx.send("Использование удобрений в сельском хозяйстве приводит к выделению закиси азота, который в 300 раз сильнее CO2 по влиянию на климат.")

# Последствия
@bot.command(name="последствие_1")
async def effect_1(ctx):
    await ctx.send("Из-за глобального потепления происходит таяние ледников и полярных льдов, что приводит к повышению уровня моря.")

@bot.command(name="последствие_2")
async def effect_2(ctx):
    await ctx.send("Климатические изменения вызывают экстремальные погодные явления, такие как ураганы, наводнения и засухи.")

@bot.command(name="последствие_3")
async def effect_3(ctx):
    await ctx.send("Повышение температуры приводит к изменению экосистем и исчезновению многих видов животных и растений.")

@bot.command(name="последствие_4")
async def effect_4(ctx):
    await ctx.send("Сельское хозяйство страдает из-за изменения климата, что приводит к снижению урожайности и продовольственным кризисам.")

@bot.command(name="последствие_5")
async def effect_5(ctx):
    await ctx.send("Таяние вечной мерзлоты в Арктике высвобождает метан, что усиливает глобальное потепление.")

@bot.event
async def on_ready():
    print(f'Бот {bot.user} готов к работе! Вводи !помощь и узнавай команды')

bot.run()
