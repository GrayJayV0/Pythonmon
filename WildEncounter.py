from TypeChart import *
from Pokemon import *
from Moves import *
from Player import *
from random import *
from copy import deepcopy
def clearConsole(): print("\033[H\033[J", end="") 
  

def wildEncounter(player, pythonmon):
  global wildPythonmon, selectedPythonmon
  wildPythonmon = deepcopy(pythonmon)
  for slot in player.Loadout:
    if player.Loadout[slot] != None:
      if player.Loadout[slot].Hp > 0:
        selectedPythonmon = player.Loadout[slot]
        break
    if slot == 'slot6':
      input('You have no pokemon to battle\n')
      return
      
  input(f'A wild {wildPythonmon.Name} attacked')
  while wildPythonmon.Hp > 0 and selectedPythonmon.Hp > 0:
    nameLine = '--'
    for i in wildPythonmon.Name:
      nameLine += '-'
    hpLine = '------'
    for i in str(wildPythonmon.Hp):
      hpLine += '-'
    enemyDisplay = f'\t\t\t\t\t\t\t\t{nameLine}{hpLine}\n\t\t\t\t\t\t\t\t {wildPythonmon.Name} | {wildPythonmon.Hp} Hp \n\t\t\t\t\t\t\t\t{nameLine}{hpLine}'

    nameLine = '--'
    for i in player.Loadout[slot].Name:
      nameLine += '-'
    hpLine = '------'
    for i in str(player.Loadout[slot].Hp):
      hpLine += '-'
    playerDisplay = f'{player.Name}\n{nameLine}{hpLine}\n {selectedPythonmon.Name} | {selectedPythonmon.Hp} Hp \n{nameLine}{hpLine}'
      
    moveLine = f' [1]{selectedPythonmon.Move[0].Name}\t[2]{selectedPythonmon.Move[1].Name} \n [3]{selectedPythonmon.Move[2].Name}\t[4]{selectedPythonmon.Move[3].Name} '
    clearConsole()
    moveChoice = print(f'{enemyDisplay}\n{playerDisplay}\n')
    
    battleChoice = input('[1]Battle [2]Party [3]Inventory [4]Run\n')
    clearConsole()
    
    if battleChoice == '1':
      moveChoice = input(f'{enemyDisplay}\n{playerDisplay}\n{moveLine}\n')
      slowChoice = moveChoice
      if moveChoice in ['1','2','3','4']:
        equalSpd = randint(1,2)
        if selectedPythonmon.Spd >= wildPythonmon.Spd and selectedPythonmon.Hp >= 0 or equalSpd == 1:
          moveChoice = int(moveChoice)-1
          if selectedPythonmon.Move[moveChoice].Stat == 'damage' or selectedPythonmon.Move[moveChoice].Stat == 'damage effect':
            if randint(1,101) in range(selectedPythonmon.Move[moveChoice].Accuracy):
              if selectedPythonmon.Move[moveChoice].Type == selectedPythonmon.Type:
                stab = 1.5
              else:
                stab = 1
                
              if randint(1,100) <= 6:
                input('Critical')
                crit = (float('1.'+str(selectedPythonmon.Lvl)))
              else:
                crit = 1 
      
              if all(selectedPythonmon.Type):
                effectiveness = selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]]
              else:
                effectiveness = selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]] * selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]]
      
              if effectiveness == 1:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was effective\n')
              elif effectiveness >= 2:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was super effective\n')
              elif effectiveness <= .5:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was ineffective\n')
              elif effectiveness == 0:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was immune\n')
              wildPythonmon.Hp -= int((effectiveness*selectedPythonmon.Move[moveChoice].Effect*((stab*crit*(selectedPythonmon.Atk/wildPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
            else:
              input(f'{selectedPythonmon.Move[moveChoice].Name} missed')
      
          while True:
            moveChoice = choice(wildPythonmon.Move)
            if moveChoice.Name != 'Blank':
              break
        
          if moveChoice.Stat == 'damage' or moveChoice.Stat == 'damage effect':
            
            if randint(1,101) in range(moveChoice.Accuracy):
              if moveChoice.Type == wildPythonmon.Type:
                stab = 1.5
              else:
                stab = 1
                
              if randint(1,100) <= 6:
                print('Critical')
                crit = (float('1.'+str(wildPythonmon.Lvl)))
              else:
                crit = 1 
        
              if all(wildPythonmon.Type):
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]]
              else:
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]] * moveChoice.Type[selectedPythonmon.Type[0]]
        
              if effectiveness == 1:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was effective\n')
              elif effectiveness >= 2:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was super effective\n')
              elif effectiveness <= .5:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was ineffective\n')
              elif effectiveness == 0:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it had no effect\n')
              selectedPythonmon.Hp -= int((effectiveness*moveChoice.Effect*((stab*crit*(wildPythonmon.Atk/selectedPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
            else:
              input(f'{moveChoice.Name} missed')

        elif selectedPythonmon.Spd <= wildPythonmon.Spd and selectedPythonmon.Hp >= 0 or equalSpd == 1:
          while True:
            moveChoice = choice(wildPythonmon.Move)
            if moveChoice.Name != 'Blank':
              break
        
          if moveChoice.Stat == 'damage' or moveChoice.Stat == 'damage effect':
            
            if randint(1,101) in range(moveChoice.Accuracy):
              if moveChoice.Type == wildPythonmon.Type:
                stab = 1.5
              else:
                stab = 1
                
              if randint(1,100) <= 6:
                print('Critical')
                crit = (float('1.'+str(wildPythonmon.Lvl)))
              else:
                crit = 1 
        
              if all(wildPythonmon.Type):
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]]
              else:
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]] * moveChoice.Type[selectedPythonmon.Type[0]]
        
              if effectiveness == 1:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was effective\n')
              elif effectiveness >= 2:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was super effective\n')
              elif effectiveness <= .5:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was ineffective\n')
              elif effectiveness == 0:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it had no effect\n')
              selectedPythonmon.Hp -= int((effectiveness*moveChoice.Effect*((stab*crit*(wildPythonmon.Atk/selectedPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
            else:
              input(f'{moveChoice.Name} missed')

          moveChoice = int(slowChoice)-1
          if selectedPythonmon.Move[moveChoice].Stat == 'damage' or selectedPythonmon.Move[moveChoice].Stat == 'damage effect':
            if randint(1,101) in range(selectedPythonmon.Move[moveChoice].Accuracy):
              if selectedPythonmon.Move[moveChoice].Type == selectedPythonmon.Type:
                stab = 1.5
              else:
                stab = 1
                
              if randint(1,100) <= 6:
                input('Critical')
                crit = (float('1.'+str(selectedPythonmon.Lvl)))
              else:
                crit = 1 
      
              if all(selectedPythonmon.Type):
                effectiveness = selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]]
              else:
                effectiveness = selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]] * selectedPythonmon.Move[moveChoice].Type[wildPythonmon.Type[0]]
      
              if effectiveness == 1:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was effective\n')
              elif effectiveness >= 2:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was super effective\n')
              elif effectiveness <= .5:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was ineffective\n')
              elif effectiveness == 0:
                input(f'{selectedPythonmon.Move[moveChoice].Name} was imunne\n')
              wildPythonmon.Hp -= int((effectiveness*selectedPythonmon.Move[moveChoice].Effect*((stab*crit*(selectedPythonmon.Atk/wildPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
            else:
              input(f'{selectedPythonmon.Move[moveChoice].Name} missed')
    
    elif battleChoice == '2':
      num = 0
      line = ''
      for slots in player.Loadout:
        num += 1
        if player.Loadout[slots] != None:
          line += f'[{num}]{player.Loadout[slots].Name}'
          if player.Loadout[slots].Hp <= 0:
            line += ' (fainted)'
        else:
          line += f'[{num}]None'
        line += '\n\n'
      while True:
        partyChoice = input(line)
        if partyChoice in ['1','2','3','4','5','6']:
          break
      
      num = 0
      for slots in player.Loadout:
        num += 1
        if int(partyChoice) == num and player.Loadout[slots] != None:
          ssChoice = input(f'{player.Loadout[slots].Name}\n[1]Switch [2]Stats [3]Cancel\n')
          if ssChoice == '1' and selectedPythonmon != player.Loadout[slots] and player.Loadout[slots].Hp > 0:
            selectedPythonmon = player.Loadout[slots]
            input(f'{selectedPythonmon.Name} switched in\n')
            
            while True:
              moveChoice = choice(wildPythonmon.Move)
              if moveChoice.Name != 'Blank':
                break
          elif ssChoice == '2':
            input('Feature coming soon')
            break
          
            if moveChoice.Stat == 'damage' or moveChoice.Stat == 'damage effect':

              if randint(1,101) in range(moveChoice.Accuracy):
                if moveChoice.Type == wildPythonmon.Type:
                  stab = 1.5
                else:
                  stab = 1

                if randint(1,100) <= 6:
                  print('Critical')
                  crit = (float('1.'+str(wildPythonmon.Lvl)))
                else:
                  crit = 1

                if all(wildPythonmon.Type):
                  effectiveness = moveChoice.Type[selectedPythonmon.Type[0]]
                else:
                  effectiveness = moveChoice.Type[selectedPythonmon.Type[0]] * moveChoice.Type[selectedPythonmon.Type[0]]

                if effectiveness == 1:
                  input(f'{wildPythonmon.Name} used {moveChoice.Name} it was effective\n')
                elif effectiveness >= 2:
                  input(f'{wildPythonmon.Name} used {moveChoice.Name} it was super effective\n')
                elif effectiveness <= .5:
                  input(f'{wildPythonmon.Name} used {moveChoice.Name} it was ineffective\n')
                elif effectiveness == 0:
                  input(f'{wildPythonmon.Name} used {moveChoice.Name} it had no effect\n')
                selectedPythonmon.Hp -= int((effectiveness*moveChoice.Effect*((stab*crit*(wildPythonmon.Atk/selectedPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))

              else:
                input(f'{moveChoice.Name} missed')
            elif ssChoice == '2':
                clearConsole()
                input(f'{selectedPythonmon.Name} lvl {selectedPythonmon.Lvl}\n{selectedPythonmon.Desc}\n\n{selectedPythonmon.Hp} Hp\n\n{selectedPythonmon.Atk} Atk\n\n{selectedPythonmon.Def} Def\n\n{selectedPythonmon.Spd} Spd\n')
                continue
          else:
            if selectedPythonmon == player.Loadout[slots]:
              input(f'{player.Loadout[slots].Name} is already in')
            else:
              continue
              input(f'{player.Loadout[slots].Name} cannot battle')
    elif battleChoice == '3':
      battleInventory(selectedPythonmon,wildPythonmon)

    elif battleChoice == '4':
      if selectedPythonmon.Spd >= pythonmon.Spd:
        if randint(1,10) > 5:
          input("You have escaped")
          return 
        else:
          input('You couldnt escape')
          clearConsole()
          while True:
            moveChoice = choice(wildPythonmon.Move)
            if moveChoice.Name != 'Blank':
              break
        
          if moveChoice.Stat == 'damage' or moveChoice.Stat == 'damage effect':
            
            if randint(1,101) in range(moveChoice.Accuracy):
              if moveChoice.Type == wildPythonmon.Type:
                stab = 1.5
              else:
                stab = 1
                
              if randint(1,100) <= 6:
                print('Critical')
                crit = (float('1.'+str(wildPythonmon.Lvl)))
              else:
                crit = 1 
        
              if all(wildPythonmon.Type):
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]]
              else:
                effectiveness = moveChoice.Type[selectedPythonmon.Type[0]] * moveChoice.Type[selectedPythonmon.Type[0]]
        
              if effectiveness == 1:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was effective\n')
              elif effectiveness >= 2:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was super effective\n')
              elif effectiveness <= .5:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it was ineffective\n')
              elif effectiveness == 0:
                input(f'{wildPythonmon.Name} used {moveChoice.Name} it had no effect\n')
              selectedPythonmon.Hp -= int((effectiveness*moveChoice.Effect*((stab*crit*(wildPythonmon.Atk/selectedPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
            else:
              input(f'{moveChoice.Name} missed')
      else:
        input('You couldnt escape')
        while True:
          moveChoice = choice(wildPythonmon.Move)
          if moveChoice.Name != 'Blank':
            break
      
        if moveChoice.Stat == 'damage' or moveChoice.Stat == 'damage effect':
          
          if randint(1,101) in range(moveChoice.Accuracy):
            if moveChoice.Type == wildPythonmon.Type:
              stab = 1.5
            else:
              stab = 1
              
            if randint(1,100) <= 6:
              print('Critical')
              crit = (float('1.'+str(wildPythonmon.Lvl)))
            else:
              crit = 1 
      
            if all(wildPythonmon.Type):
              effectiveness = moveChoice.Type[selectedPythonmon.Type[0]]
            else:
              effectiveness = moveChoice.Type[selectedPythonmon.Type[0]] * moveChoice.Type[selectedPythonmon.Type[0]]
      
            if effectiveness == 1:
              input(f'{wildPythonmon.Name} used {moveChoice.Name} it was effective\n')
            elif effectiveness >= 2:
              input(f'{wildPythonmon.Name} used {moveChoice.Name} it was super effective\n')
            elif effectiveness <= .5:
              input(f'{wildPythonmon.Name} used {moveChoice.Name} it was ineffective\n')
            elif effectiveness == 0:
              input(f'{wildPythonmon.Name} used {moveChoice.Name} it had no effect\n')
            selectedPythonmon.Hp -= int((effectiveness*moveChoice.Effect*((stab*crit*(wildPythonmon.Atk/selectedPythonmon.Def)+1))) * float('0.1'+ str(randint(1,255))))
          else:
            input(f'{moveChoice.Name} missed')

    while selectedPythonmon.Hp <= 0:
      num = 0
      line = ''
      for slots in player.Loadout:
        num += 1
        if player.Loadout[slots] != None:
          line += f'[{num}]{player.Loadout[slots].Name}'
          if player.Loadout[slots].Hp <= 0:
            line += ' (fainted)'
        else:
          line += f'[{num}]None'
        line += '\n\n'
      while True:
        clearConsole()
        print(f'{selectedPythonmon.Name} has fainted')
        partyChoice = input(line)
        if partyChoice in ['1','2','3','4','5','6']:
          break
      
      num = 0
      for slots in player.Loadout:
        num += 1
        if int(partyChoice) == num and player.Loadout[slots] != None:
          ssChoice = input(f'{player.Loadout[slots].Name}\n[1]Switch [2]Stats [3]Cancel\n')
          if ssChoice == '1' and selectedPythonmon != player.Loadout[slots] and player.Loadout[slots].Hp > 0:
            selectedPythonmon = player.Loadout[slots]
            input(f'{selectedPythonmon.Name} switched in\n')
          else:
            input(f'{player.Loadout[slots].Name} cannot battle')
            continue
  if wildPythonmon.Hp > 0:
    print('You lost')
  elif wildPythonmon.Hp <= 0:
    print('You have won')