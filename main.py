#chatbot + discord
import discord
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

from chatterbot.response_selection import get_random_response

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

conv = open('./train/traindata.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(
#  "./train/conversation.yml"
#)
#End ChatBot

ste = False

client = discord.Client()

@client.event
async def on_ready():
  print('Ta bien {0.user} '.format(client))

@client.event
async def on_message(message):
  msg = message.content
  global ste
  print(msg)
  #print(message.channel)

  #boti = bot.get_response(str(message.content))
  #print(boti)
  #await message.reply(boti)

  if message.author == client.user:
    return
  else:
    if msg.startswith('$gracias por la charla'):
      await message.channel.send('Gracias a ti ! :D espero hablar contigo denuevo')
      ste = False

    if msg.startswith('$hola'):
      await message.channel.send('Hola bobo')

    if msg.startswith('$charlemos'):
      await message.channel.send('Ok, hablemos por un momento')
      ste = True

    if msg.includes('1zumi' or 'izumi'):
      await message.channel.send('Si! {message.author} soy yo DIO')

    if msg.includes('sad' or 'triste' or 'me quiero matar'):
      await message.channel.send('no tienes que estar sad {message.author}, yo SIEMPRE estaré aqui para ti :3`')

    if msg.startswith('ZA WARDO'):
      await message.channel.send('TOKI WO TOMAREEEEEEE')

    if ste == True:
      bot_input = bot.get_response(msg)
      print(bot_input)
      await message.reply(bot_input)

  #video discord 21:18

client.run(os.getenv('TOKEN'))