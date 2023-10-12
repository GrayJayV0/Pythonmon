from TypeChart import *
from random import *
from Player import *
from Func import *
from copy import deepcopy
class Item:
  def __init__(self, Name, Description, Uses, Effect = None):
    self.Name = Name
    self.Description = Description
    self.Uses = Uses
    self.Effect = Effect


def catch(name,pokemon,wildPokemon,player):
  Typewrite(f'You threw a {name}\n')
  if name == "Pokeball":
    ball = randint(1,256)
    catchChance = (wildPokemon.Max*255*4)/(wildPokemon.Hp*ball)
    shakes = (wildPokemon.CatchRate*100/ball)*(catchChance)/255
    if shakes < 10:
      Typewrite('miss\n')
      input()
      return
    elif shakes < 30:
      Typewrite('shake\n')
    elif shakes < 70:
      for i in range(2):
        Typewrite('shake\n')
    else:
      for i in range(3):
        Typewrite('shake\n')
    if catchChance >= ball:
      Typewrite('catch\n')
      for slots in player.Loadout:
        if player.Loadout[slots] == None:
          Typewrite(f'{wildPokemon.Name} was added to your party\n')
          input()
          player.Loadout[slots] = deepcopy(wildPokemon)
          wildPokemon.Hp = 0
          return wildPokemon
      Typewrite(f'{wildPokemon.Name} was added to your pc\n')
      input()
      return
    else:
      Typewrite('broke free\n')
      input()

pokeball = Item('Pokeball',"A device for catching wild Pokémon. It's thrown like a ball at a Pokémon, comfortably encapsulating its target.",['battleInventory'], catch)
