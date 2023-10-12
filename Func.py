import time
import sys

def clearConsole(): print("\033[H\033[J", end="") 

import time
typeTickMultiplier = .09
def Typewrite(write, delay=1):
  for i in write:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(delay * typeTickMultiplier)