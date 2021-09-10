import time, os, sys, keyboard, cv2
from ahk import AHK
from metin2.mt2 import game

def main():
  last_time = time.time()-10

  while True:
   
    if time.time()-last_time >= 0.5 :   #controla o game loop 0.5/s
      last_time = time.time()

      game.start_pot()
      game.start_drop()

    if keyboard.is_pressed('q'):
        print('close')
        sys.exit() 

  
if __name__ == "__main__":
  main()   
    