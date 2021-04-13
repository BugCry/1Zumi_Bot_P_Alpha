#chatbot + discord
import discord
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

from chatterbot.response_selection import get_random_response

from keep_alive import keep_alive

#metodos


#ChatBot
bot = ChatBot(
    '1ZUMI',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

#conv = open('./train/short_traindata.txt', 'r').readlines()
#bot.set_trainer(ListTrainer)
#bot.train(conv)

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(
#  "./train/traindata375y.yml"
#)
#End ChatBot

ste = False
firstT = True

client = discord.Client()

@client.event
async def on_ready():
  print('Ta bien {0.user} '.format(client))

@client.event
async def on_message(message):
  msg = message.content
  global ste
  global firstT
  print(msg)
  #print(message.channel)

  #boti = bot.get_response(str(message.content))
  #print(boti)
  #await message.reply(boti)

  if message.author == client.user:
    return
  else:
    if firstT == True:
      await message.reply('Hola al parecer eres la primera persona con la que hablo desde que me activé')
      await message.channel.send('Si quieres saber mas de mi funcionamiento usa el comando: $1ZUMI -h')
      firstT = False

    if msg.startswith('$gracias por la charla'):
      await message.channel.send('Gracias a ti ! :D espero hablar contigo denuevo')
      ste = False

    if msg.startswith('$hola'):
      await message.channel.send('Hola bobo')

    if msg.startswith('$1ZUMI'):
      await message.channel.send('Pues que te digo ...')
      await message.channel.send('¡Hola! Soy 1ZUMI tu asistente personal ... mas o menos ...')
      await message.channel.send('por el momento te dejaré los comandos que puedes usar')
      await message.channel.send('-h                            Muestra ayuda sobre el funcionamiento de la aplicacion')
      await message.channel.send('$charlemos                  Activa el modo ChatBot')
      await message.channel.send('$gracias por la charla   Termina el proceso del chatbot')
      return

    if msg.startswith('$charlemos'):
      await message.channel.send('Ok, hablemos por un momento')
      ste = True

    if '1zumi' in msg.lower():
      await message.channel.send('Si! {message.author} soy yo DIO')

    if msg.startswith('sad' or 'triste' or 'me quiero matar'):
      await message.channel.send('no tienes que estar sad {message.author}, yo SIEMPRE estaré aqui para ti :3`')

    if msg.startswith('ZA WARDO'):
      await message.channel.send('TOKI WO TOMAREEEEEEE')

    if ste == True and not msg.startswith('$'):
      bot_input = bot.get_response(msg)
      print(bot_input)
      if 'current' in str(bot_input):
        await message.channel.send('Lo siento, estaba pensando en decir algo estupido')
      else:
        await message.reply(bot_input)

  #video discord 21:18

keep_alive()
client.run(os.getenv('TOKEN'))