from TypeChart import *
from random import *
from Player import *
from copy import deepcopy
class Item:
  def __init__(self, Name, Description, Uses, Effect = None):
    self.Name = Name
    self.Description = Description
    self.Uses = Uses
    self.Effect = Effect


def catch(name,pokemon,wildPokemon,player):
  if name == "Pokeball":
    ball = randint(1,256)
    catchChance = (wildPokemon.Max*255*4)/(wildPokemon.Hp*ball)
    shakes = (wildPokemon.CatchRate*100/ball)*(catchChance)/255
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
      for slots in player.Loadout:
        if player.Loadout[slots] == None:
          print(f'{wildPokemon.Name} was added to your party')
          player.Loadout[slots] = deepcopy(wildPokemon)
          wildPokemon.Hp = 0
          return wildPokemon
      print(f'{wildPokemon.Name} was added to your pc')
      return
    else:
      print('broke free')

pokeball = Item('Pokeball',None,['battleInventory'], catch)
