from TypeChart import *
from Pokemon import *
from Item import *
from copy import deepcopy
def clearConsole(): print("\033[H\033[J", end="") 

class Player:
  def __init__(self, Name, Loadout, Inventory):
    self.Name = Name
    self.Loadout = Loadout
    self.Inventory = Inventory

protagonist = Player('Jayden', {'slot1':None,'slot2':deepcopy(bulbasaur) ,'slot3':deepcopy(charmander),'slot4':None,'slot5':None,'slot6':None}, [pokeball])

def battleInventory():
  while True:
    while True:
      a = {}
      index = 0
      end = 1
      clearConsole()
      print("Your Inventory")
      # Assigns a number to each inventory item
      for space in protagonist.Inventory:
        index += 1
        end += 1
        a += str(index):space,
        print(f"[ {index} ] {space.Name[0]}")
      a.append(str(end))
      choice = input(f"\n[ {end} ] Leave Inventory\n")
      clearConsole()
      if choice in a:
        a.clear()
        break

    # If the last number is inputted leaves inventory
    if choice == str(end):
      return
    else:
      while True:
        clearConsole()
        print(protagonist.Inventory[int(choice)-1].Name + "\n" + protagonist.Inventory[int(choice)-1].description + "\n")
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