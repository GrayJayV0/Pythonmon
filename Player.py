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

def battleInventory(selectedPythonmon, wildPythonmon):
  while True:
    while True:
      inventoryChoice = {}
      index = 0
      end = 1
      clearConsole()
      print("Your Inventory")
      # Assigns a number to each inventory item
      for space in protagonist.Inventory:
        index += 1
        end += 1
        inventoryChoice.update({str(index): space})
        print(f"[ {index} ] {space.Name}")
      choice = input(f"\n[ {end} ] Leave Inventory\n")
      clearConsole()
      if choice in inventoryChoice or choice == str(end):
        inventoryChoice = inventoryChoice[choice]
        break

    # If the last number is inputted leaves inventory
    if choice == str(end):
      return
    else:
      while True:
        clearConsole()
        print(f"{inventoryChoice.Name}\n{inventoryChoice.Description}\n")
        choice2 = input("[1]Use\n[2]Leave\n")
        if choice2 not in ["1","2"]:
          continue

        if choice2 == "1" and 'battleInventory' in inventoryChoice.Uses:
          inventoryChoice.Effect(inventoryChoice.Name,selectedPythonmon,wildPythonmon,protagonist)
          protagonist.Inventory.remove(inventoryChoice)
          return