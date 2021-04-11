import discord
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

from chatterbot.response_selection import get_random_response

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

client = discord.Client()

@client.event
async def on_ready():
  print('Ta bien {0.user} '.format(client))

@client.event
async def on_message(message):
  print(message.content)
  #print(message.channel)

  #boti = bot.get_response(str(message.content))
  #print(boti)
  #await message.reply(boti)

  if message.author == client.user:
    return
  else:
    bot_input = bot.get_response(message.content)
    print(bot_input)
    await message.reply(bot_input)

  if message.content.startswith('$hola'):
    await message.channel.send('Hola bobo')

  #video discord 21:18

client.run(os.getenv('TOKEN'))