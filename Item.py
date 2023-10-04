from TypeChart import *
from random import *
from Player import *
from copy import deepcopy

class Item:
  def __init__(self, name, description, effect):
    self.name = name,
    self.description = description,
    self.effect = effect

pokeball = Item('pokeball',None,None)

def catch(name,max,pokemon):
  if name == "pokeball":
    ball = randint(1,256)
    catchChance = (max*255*4)/(pokemon.Hp*ball)
    shakes = (pokemon.CatchRate*100/ball)*(catchChance)/255
    if shakes < 10:
      print('miss')
      return
    elif shakes < 30:
      print('shake once')
    elif shakes < 70:
      print('shake twice')
    else:
      print('shake thrice')
    if catchChance >= ball:
      print('catch')
      for slots in protagonist.Loadout:
        if protagonist.Loadout[slots] == None:
          print(f'{pokemon.Name} was added to your party')
          protagonist.Loadout[slots] = deepcopy(pokemon)
          return
      print(f'{pokemon.Name} was added to your pc')
      return
    else:
      print('broke free')