import random
from time import sleep

# variables
coins = 2
multiflip = 0
loop = True
the_coin_list = []
debug = False # turn this to True if you wanna skip the delays

# to check and save what the player choosen
def check_choice(user_input):
   global coins, multiflip
   if user_input in ["head","heads","h","1"]:
      return "Heads"
   elif user_input in ["tails","tail","t","2"]:
      return "Tails"
   elif user_input in ["add","add coins","multiflip","a","3"] and coins > 1 and multiflip < 3:
      coins -= 1
      multiflip += 1
      return True
   else:
      return None

# decide if the coin is heads or tails
def get_coin():
   the_coin = ""
   the_coin = random.choice(["Heads", "Tails"])
   if not debug:
      sleep(0.8)
   print(f"[game]: the coin lands on... {the_coin}!")
   if not debug:
      sleep(2)
   return the_coin

# epic spin animation
def spinning_anim():
    spin_frames = ["\\", "|", "/", "-"]
    for _ in range(3):
       for frame in spin_frames:
          print(f"spinning... {frame}", end="\r",flush=True)
          sleep(0.1)

# multispin animation
def multi_anim():
   global multiflip
   counter = 0
   while counter <= multiflip:
      print(f" flipping... {counter} out of {multiflip}")
      counter += 1
      if not debug:
         sleep(0.3)
   print("flipping completed")

# insructions
print("[game]: Your goal is to get 5 coins, if you lose it all, well... you lose.")
if not debug:
   sleep(3)
print("[game]: anyway take these 2 coins with you, goodluck !")
if not debug:
   sleep(3)

# main interface/ loop
while loop:
   print("\n------------------")
   print(f"You have {coins} coins\nmultiflipping {multiflip} coins")
   print("------------------")
   print("\n" + "=" * 24)
   print("[game]: Heads or tails?")
   print("  (1) Heads")
   print("  (2) Tails")
   print("  (3) Add coins to multiflip")
# users input
   h_t = str(input("> ")).lower()

   print("_" * 30)

# saving coin choice
   coin_c = check_choice(h_t)

# if the input is multiflip or invalid
   if coin_c == True:
      print("[system]: Adding a coin to multiflip...")
      continue
   elif coin_c == None:
      print("[system]: this action isnt available...")
      continue

# build up suspension
   print(f"[system]: You have chosen... {coin_c}")
   if not debug:
      sleep(1)
   print("[game]: lets see you luck!")
   if not debug:
      sleep(0.6)

# different animation for multiflip and singular flip
   if multiflip > 0:
      multi_anim()
      for _ in range(multiflip + 1):
         the_coin_list.append(get_coin())
   else:
      spinning_anim()
      the_coin_list.append(get_coin())

# decides if player won or not 
   num_wins = sum(1 for coin in the_coin_list if coin == coin_c)
   if num_wins > 0:
      print(f"[game]: winner !! You won {num_wins} times!")
      coins += num_wins
      multiflip = 0
      if not debug:
         sleep(2)
   else:
      print("[game]: how unlucky...")
      coins -= 1
      multiflip = 0
      if not debug:
         sleep(2)

# clear the list for the next round
   the_coin_list.clear()

# letting know the loop when to stop when the conditions are met
   if coins == 0:
      loop = False
   elif coins >= 5:
      loop = False

# out of coins
if coins == 0:
   print("[game]: you lost...")
elif coins >= 5:
   print("[game]: thank you so much for playing ><, this was such a fun little project i made, if you want to add anything else; please contact:3 thank youu !!")