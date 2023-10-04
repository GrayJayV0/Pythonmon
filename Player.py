from TypeChart import *
from Pokemon import *
from Item import *
from copy import deepcopy
def clearConsole(): print("\033[H\033[J", end="") 

class Player:
  def __init__(self, Name = None, Loadout = {'slot1':None,'slot2':deepcopy(bulbasaur) ,'slot3':deepcopy(charmander),'slot4':None,'slot5':None,'slot6':None}, Inventory = [pokeball]):
    self.Name = Name
    self.Loadout = Loadout
    self.Inventory = Inventory

protagonist = Player('Jayden')

def inventory():
  a = []
  end = 1
  while True:
    while True:
      clearConsole()
      # Shows what items you have equipped
      print("Your Inventory")
      # Assigns a number to each inventory item
      for space in protagonist.Inventory:
        a.append(str(end+1))
        print("[" + str(i+1) + "] " + protagonist.Inventory['space'].name)
        # end = i + 2
      a.append(str(end))
      choice = input("\n[" + str(end) + "]" +"Leave Inventory\n")
      clearConsole()
      print(choice)
      if choice in a:
        a.clear()
        break
      else:
        a.clear()
        continue
    # If the last number is inputted leaves inventory
    if choice == str(end):
      return
    else:
      while True:
        clearConsole()
        print(protagonist.Inventory[int(choice)-1].name + "\n" + protagonist.Inventory[int(choice)-1].description + "\n")
        choice2 = input("[1]Use\n[2]Leave\n")
        if choice2 not in ["1","2"]:
          continue
        # Equips the item and checks what type of item it is
        if choice2 == "1" and protagonist.Inventory[int(choice)-1] not in protagonist.equip and protagonist.Inventory[int(choice)-1] in armour:
          protagonist.Inventory.append(protagonist.equip[1])
          protagonist.equip[1] = protagonist.Inventory[int(choice)-1]
          protagonist.Inventory.remove(protagonist.Inventory[int(choice)-1])
          clearConsole() 
          break
          
        # Equips the item and checks what type of item it is
        elif choice2 == "1" and protagonist.Inventory[int(choice)-1] not in protagonist.equip and protagonist.Inventory[int(choice)-1] in weapon:
          protagonist.Inventory.append(protagonist.equip[0])
          protagonist.equip[0] = protagonist.Inventory[int(choice)-1]
          protagonist.Inventory.remove(protagonist.Inventory[int(choice)-1])
          clearConsole()
          break
        elif choice2 == "1" and protagonist.Inventory[int(choice)-1] not in protagonist.equip and protagonist.Inventory[int(choice)-1] in item:
          protagonist.Inventory[int(choice)-1].effect()
          protagonist.Inventory.remove(protagonist.Inventory[int(choice)-1])
          clearConsole()
          break
        # Leaves this inventory screen
        elif choice2 == "2":
          clearConsole()
          break
        # If the item is already equipped
        else:
          clearConsole()