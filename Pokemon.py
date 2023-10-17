import random

from TypeChart import *
from Moves import *
from Func import *
import math
pythonmon = {}
class Pokemon:
  def __init__(self, Name, Max, Hp, Atk, Def, Spd, Move, Type,  Desc, CatchRate, Xp, LvlRate, Item = None, MoveList = None):
    self.Name = Name
    self.Max = Max
    self.Hp = Hp
    self.Atk = Atk
    self.Def = Def
    self.Spd = Spd
    self.Move = Move
    self.Type = Type
    self.Desc = Desc
    self.Item = Item
    self.CatchRate = CatchRate
    self.LvlRate = LvlRate
    self.Xp = Xp
    self.MoveList = MoveList
    self.Lvl = 1
    self.DVHP = random.randint(1,15)
    self.DVATK = random.randint(1, 15)
    self.DVDEF = random.randint(1, 15)
    self.DVSPD = random.randint(1, 15)
    pythonmon[self.Name] = self
    self.statCalc()
    self.Hp = self.Max
  def lvlCalc(self):
    if self.LvlRate == 'fast':
      experience = self.Xp
      level = ((experience*5)/4)**(1/3)
      self.Lvl = int(level)

  def statCalc(self):
    default = pythonmon[self.Name]
    self.lvlCalc()
    self.Max = int(((((default.Hp + self.DVHP) * 2 + (math.sqrt(252))/4)* self.Lvl) / 100) + self.Lvl + 10)
    self.Atk = int(((((default.Atk + self.DVATK) * 2 + (math.sqrt(252))/4) * self.Lvl) / 100) + 5)
    self.Def = int(((((default.Def + self.DVDEF) * 2 + 252/4) * self.Lvl) / 100) + 5)
    self.Spd = int(((((default.Spd + self.DVSPD) * 2 + (math.sqrt(252))/4) * self.Lvl) / 100) + 5)

  def __str__(self):
    return f'Name:{self.Name} Max Hp:{self.Max} Current Hp:{self.Hp} Atk:{self.Atk} Def:{self.Def} Spd:{self.Spd} Type:{self.Type} Level:{self.Lvl}'







squirtle = Pokemon('Squirtle', 44, 44
                   , 5, 65, 43, [tackle,waterGun,blank,blank], ['water'], 5, 'Shoots water at prey while in the water. Withdraws into its shell when in danger', 50000, 'fast')

charmander = Pokemon('Charmander', 39, 39
, 52, 43, 65, [scratch,ember,blank,blank], ['fire'], 5, 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.', 45, 'fast')

bulbasaur = Pokemon('Bulbasaur', 45, 45, 49, 49, 45, [tackle,vineWhip,blank,blank], ['grass','poison'], 5, 'A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.', 800001, 'fast')
