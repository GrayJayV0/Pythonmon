from TypeChart import *


class Move:
  def __init__(self, Name, Effect, Type, Accuracy, Stat):
    self.Name = Name
    self.Effect = Effect
    self.Type = Type
    self.Accuracy = Accuracy
    self.Stat = Stat

tackle = Move('Tackle', 40, normal, 100, 'damage')
scratch = Move('Scratch', 40, normal, 100, 'damage')
waterGun = Move('Water Gun', 40, water, 100, 'damage')
thunderShock =  Move('Thunder Shock', 20, electric, 100, 'damage effect')
vineWhip = Move('Vine Whip', 40, grass, 100, 'damage')
ember =  Move('Ember', 20, fire, 100, 'damage effect')

blank =  Move('Blank',None,None,None,None)