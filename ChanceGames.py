import random

money = 100

def endgame(bet,outcome):
  if outcome == "win":
    print("WINNER!\nYou win {} dollars.".format(bet))
    return bet
  elif outcome == "lose":
    print("LOSER!\nYou lose {} dollar.".format(bet))
    return bet*-1
  elif outcome == "tie":
    print("TIE!\nYou keep your money.")
    return 0

#Write your game of chance functions here

def coin_flip(bet, choice):
  flip = random.randint(0,1)
  if "heads" in choice.lower():
    choice == "heads"
  else:
    choice == "tails"
  print("CHOICE: " + choice.upper())
  if flip == 0:
    print("FLIP: TAILS")
  else:
    print("FLIP: HEADS")
    
  if (flip == 0 and choice == "tails") or (flip == 1 and choice == "heads"):
    return endgame(bet, "win")
  else:
    return endgame(bet, "lose")
    
def cho_han(bet, choice):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  total = dice1 + dice2
  if "odd" in choice.lower():
    print("HAN! はん!")
    choice = "odd"
  else:
    print("CHO! ちょう!")
    choice = "even"
  print("CHO HAN\nDICE 1: {} || DICE 2: {} || TOTAL: {}".format(str(dice1), str(dice2), str(total)))
  
  if total % 2 == 0:
    print("HAN! はん!")
  else:
    print("CHO! ちょう!")
  
  if (choice == "odd" and total % 2 == 1) or (choice == "even" and total % 2 == 0):
    return endgame(bet, "win")
  else:
    return endgame(bet, "lose")
  
def card_war(bet):
  deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
  random.shuffle(deck)
  player1 = deck.pop()
  player2 = deck.pop()
  print("CARD WAR\nPLAYER HAS: {}\nCOMPUTER HAS: {}".format(str(player1), str(player2)))
  if player1 > player2:
    return endgame(bet, "win")
  elif player1 < player2:
    return endgame(bet, "lose")
  else:
    return endgame(bet, "tie")
  
def roulette(bet, choice):
  if "odd" in choice.lower():
    choice = "odd"
    choiceType = "oddeven"
  elif "even" in choice.lower():
    choice = "even"
    choiceType = "oddeven"
  else:
    choiceType = "number"
  roll = random.randint(-1,36)
  print("PLAYER HAS CHOSEN: {}\nROLL IS: {}".format(choice, str(roll)))
  if choiceType == "oddeven":
    if (choice == "odd" and roll > 1 and roll % 2 == 1) or (choice == "even" and roll > 1 and roll % 2 == 0):
      return endgame(bet, "win")
    else:
      return endgame(bet, "lose")
  else:
    if choice == "00" and roll == -1:
      return endgame(bet*5, "win")
    elif choice == "0" and roll == 0:
      return endgame(bet*3, "win")
    elif int(choice) == roll:
      return endgame(bet*2, "win")
    else:
      return endgame(bet, "lose")
      
#Call your game of chance functions here

print("WELCOME TO MIKA'S GAMES OF CHANCE!\n")
print("Other games by Mika: Blackjack, Go Fish, Pass the Pig, Texas Hold Em', Tic Tac Toe, Uno, Connect 4, War, Hangman, and Anagram.\n")
print("GAMES OFFERED HERE: Coin Flip, Cho-Han, Card War, and Roulette.\n")
print("Coin Flip:\nFlip a coin and guess correctly out of HEADS and TAILS to win!")
print("Cho-Han:\nRoll two dice and guess correctly out of ODD and EVEN to win!")
print("Card War:\nPick a card and see if it is higher than the computer's card to win!")
print("Roulette:\nSpin the wheel and see if your guess between ODD, EVEN, 00, or 0-36 is correct to win!")
print("To quit at any time, enter quit when asked about the game to play.")

while True:
  gameChoice = input("What game would you like to play? >> ")
  gameChoice = gameChoice.lower()
  if "coin" in gameChoice:
    while True:
      choice = input("Would you like HEADS, or TAILS? >> ")
      choice = choice.lower()
      if "heads" in choice or "tails" in choice:
        break
      else:
        continue
    bet = int(input("How much would you like to bet? >> "))
    money += coin_flip(bet, choice)
  elif "cho" in gameChoice:
    while True:
      choice = input("Would you like ODD, or EVEN? >> ")
      choice = choice.lower()
      if "odd" in choice or "even" in choice:
        break
      else:
        continue
    bet = int(input("How much would you like to bet? >> "))
    money += cho_han(bet, choice)
  elif "card" in gameChoice:
    bet = int(input("How much would you like to bet? >> "))
    money += card_war(bet)
  elif "roulette" in gameChoice:
    choice = input("Would you like ODD, EVEN, 00, or a number between 0 and 36? >> ")
    bet = int(input("How much would you like to bet? >> "))
    money += roulette(bet, choice)
  elif "quit" in gameChoice:
    break
  else:
    print("That is not a valid game choice.")