from TypeChart import *
from Moves import *
from Func import *

class Pokemon:
  def __init__(self, Name, Max, Hp, Atk, Def, Spd, Move, Type, Lvl, Desc, CatchRate, Xp = None, Item = None):
    self.Name = Name
    self.Max = Max
    self.Hp = Hp
    self.Atk = Atk
    self.Def = Def 
    self.Spd = Spd
    self.Move = Move
    self.Type = Type
    self.Lvl = Lvl
    self.Desc = Desc
    self.Item = Item 
    self.Xp = Xp
    self.CatchRate = CatchRate

squirtle = Pokemon('Squirtle', 44, 44
                   , 48, 65, 43, [tackle,waterGun,blank,blank], ['water'], 5, 'Shoots water at prey while in the water. Withdraws into its shell when in danger', 45)

charmander = Pokemon('Charmander', 39, 39
, 52, 43, 65, [scratch,ember,blank,blank], ['fire'], 5, 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.', 45)

bulbasaur = Pokemon('Bulbasaur', 45, 45, 49, 49, 45, [tackle,vineWhip,blank,blank], ['grass','poison'], 5, 'A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.', 45)