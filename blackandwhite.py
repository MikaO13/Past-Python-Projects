from getpass import getpass
import random

# text = getpass("Enter text: ", stream=None)
# text = input("Enter text: ")

p1_name = ""
p2_name = ""

p1_score = 0
p2_score = 0

p1_tiles = [1,2,3,4,5,6,7,8]
p2_tiles = [1,2,3,4,5,6,7,8]

p1_bid = 0
p2_bid = 0

p1_start = False
p2_start = False

# randomly select starting player in Round 1
if random.choice([0, 1]) == 1:
    p1_start = True
else:
    p2_start = True

def print_bid_info(bid, player_name):
    # info about digits
    if bid % 2 == 0:
        print(player_name + " played a Black tile.\n")
    else:
        print(player_name + " played a White tile.\n")

def declare_round_winner(p1_bid, p2_bid):
    global p1_start
    global p2_start
    global p1_score
    global p2_score

    # tie
    if p1_bid == p2_bid:
        # p2 starts next round
        if p1_start:
            p1_start = False
            p2_start = True
            print(p1_name + " and " + p2_name + " have tied in Round " + str(round) + ". " + p2_name + " will be the starting player in Round " + str(round+1) + ".\n")
        # p1 starts next round
        else:
            p1_start = True
            p2_start = False
            print(p1_name + " and " + p2_name + " have tied in Round " + str(round) + ". " + p1_name + " will be the starting player in Round " + str(round+1) + ".\n")
    # p1 won current round
    elif p1_bid > p2_bid:
        p1_score = p1_score + 1
        p1_start = True
        p2_start = False
        print(p1_name + " has won Round " + str(round) + " and will be the starting player in Round " + str(round+1) + ".\n")
    # p2 won current round
    else:
        p2_score = p2_score + 1
        p1_start = False
        p2_start = True
        print(p2_name + " has won Round " + str(round) + " and will be the starting player in Round " + str(round+1) + ".\n")

def get_bid(player):
    global p1_bid
    global p2_bid
    global p1_tiles
    global p2_tiles

    if player == 1:
        p1_bid = getpass(p1_name + ", please enter your tile number: ", stream=None)
        error_check_bid(p1_bid, p1_tiles, 1)
        p1_bid = int(p1_bid)
        if p1_bid in p1_tiles:
            p1_tiles.remove(p1_bid)
    else:
        p2_bid = getpass(p2_name + ", please enter your tile number: ", stream=None)
        error_check_bid(p2_bid, p2_tiles, 2)
        p2_bid = int(p2_bid)
        if p2_bid in p2_tiles:
            p2_tiles.remove(p2_bid)

# tiny error handling
def error_check_bid(bid, tiles, player):
    # input not digit
    if not bid.isdigit():
        print("Error: Please enter a number.\n")
        get_bid(player)
        return True

    # check for invalid bids
    if not (int(bid) in tiles):
        print("That bid is invalid. Please rebid.\n")
        get_bid(player)
        return True
    else:
        return False

p1_name = input("Player 1, please enter your name: ")
p2_name = input("Player 2, please enter your name: ")

print()

print("The game is starting...\n")

for round in range(1,10):
    if p1_score >= 5 or p2_score >= 5:
        break

    print("Round " + str(round) + " has started.\n")

    if p1_start:
        get_bid(1)
        print("Thank you!\n")
        print_bid_info(p1_bid, p1_name)
        get_bid(2)
        print("Thank you!\n")
        print_bid_info(p2_bid, p2_name)
    else:
        get_bid(2)
        print("Thank you!\n")
        print_bid_info(p2_bid, p2_name)
        get_bid(1)
        print("Thank you!\n")
        print_bid_info(p1_bid, p1_name)

    print("--------------------------------------\n")
    print("Round " + str(round) + " has completed!\n")

    declare_round_winner(p1_bid, p2_bid)

    print(p1_name + " has " + str(p1_score) + " wins.")
    print(p2_name + " has " + str(p2_score) + " wins.\n")
    print("--------------------------------------\n")

print(p1_name + " scored " + str(p1_score) + " wins in total.")
print(p2_name + " scored " + str(p2_score) + " wins in total.\n")

if p1_score > p2_score:
    print(p1_name + " is the winner!\n")
else:
    print(p2_name + " is the winner!\n")

print("Thank you for playing!\n")
