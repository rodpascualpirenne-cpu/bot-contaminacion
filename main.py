import discord
from discord.ext import commands
import os,random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def Que_es_la_contaminacion(ctx):
    await ctx.send("La contaminación ocurre cuando ensuciamos la naturaleza con basura, humo o químicos dañinos. Esto arruina el aire, el agua y la tierra, y termina afectando la salud de animales, plantas y personas.")

@bot.command()
async def Cuales_son_sus_problemas_y_causas(ctx):
    await ctx.send("La contaminación es un problema ambiental causado principalmente por las actividades humanas, como el uso de vehículos, las industrias, la quema de combustibles fósiles, la acumulación de basura y la deforestación. Sus efectos afectan al aire, al agua y al suelo, provocando enfermedades, daños a los ecosistemas, pérdida de biodiversidad y contribuyendo al cambio climático. Por ello, es importante adoptar hábitos responsables como reciclar, reducir residuos y cuidar los recursos naturales para proteger el medio ambiente.")

@bot.command()
async def Como_puedo_reducir_la_contaminacion(ctx):
    await ctx.send("Para reducir la contaminación, puedes realizar acciones sencillas en tu vida diaria, como reciclar y reutilizar materiales, ahorrar agua y electricidad, usar el transporte público, caminar o ir en bicicleta en lugar de usar el coche, evitar el uso excesivo de plásticos y no tirar basura en la calle o en espacios naturales. Además, plantar árboles y cuidar las áreas verdes ayuda a mejorar la calidad del aire. Con pequeños cambios en nuestros hábitos, todos podemos contribuir a proteger el medio ambiente y reducir la contaminación. 🌱♻️🚲")

@bot.command()
async def Gracias(ctx):
    await ctx.send("¡De nada! 😊")

bot.run('CODIGO SECRETO!!!!')
