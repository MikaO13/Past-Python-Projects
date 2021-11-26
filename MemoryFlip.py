from string import ascii_uppercase
import random
import os

values = ["01", "01", "01", "01", "02", "02", "02", "02", "03", "03", "03", "03", "04", "04", "04", "04", 
          "05", "05", "05", "05", "06", "06", "06", "06", "07", "07", "07", "07", "08", "08", "08", "08", 
          "09", "09", "09", "09", "10", "10", "10", "10", "11", "11", "11", "11", "12", "12", "13", "13", 
          "14", "14", "15", "15", "16", "16", "17", "17", "18", "18", "19", "19", "20", "20", "20", "20"]

class Piece():
    
    def __init__(self, value, col, row):
        self.value = value
        self.col = col
        self.row = row
        self.hidden = True
        self.done = False
    
    def __str__(self):
        if self.done:
            return "||"
        elif self.hidden:
            return "XX"
        else:
            return self.value
    
    def print_value(self):
        return "{} is located at {}{}".format(self.value, self.col, self.row)

class Board():
    
    def __init__(self):
        self.board = []
        self.values = values
        self.done = False
        self.doneCards = 0
    
    def deal_pieces(self):
        for row in range(1,9):
            for col in ascii_uppercase[:8]:
                value = self.values.pop(random.randint(0,len(self.values)-1))
                self.board.append(Piece(value, col, row))
    
    def print_board(self):
        print("  ",end=" ")
        for let in ascii_uppercase[:8]:
            print(let, end = "  ")
        print("")
        for row in range(1,9):
            print(row,end="  ")
            for col in range(8):
                print(self.board[(row-1)*8+col],end=" ")
            print("")

class Player():
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def __str__(self):
        return "{} has {} points.".format(self.name, self.score)

def name_player(default):
    global forbiddenames
    name = input("What would you like to be called? >> ")
    if name in forbiddenames:
        name == default
    forbiddenames.append(name)
    return name 

def ask_card(name, board):
    while True:
        choice = input("What card would you like to open? >> ")
        if choice[0].upper() in ascii_uppercase[:8] and int(choice[1]) in range(1,9):
            break
        else:
            print("Input must be in CR, with C as a letter between A and H as the column and R being a number between 1 and 8 as the row.")
            continue
    print("{} has chosen {}.".format(name, choice))
    
    card_choice = board.board[(int(choice[1])-1)*8+ord(choice[0].upper())-64]
    
    return card_choice

def memoryflip(first_time = True, pick_players = True):
    global forbiddenames
    global players
    
    board = Board()
    board.deal_pieces()
    
    forbiddenames = []
    
    turn = 0
    
    if first_time:
        print("Welcome to Mika's Memory Flip!"
              "Here you will enjoy a game of "
              "memorization where the goal is "
              "to find the most pairs.")
        print('Other games by Mika: Texas Hold Em, Let It Ride, Seven Card Stud, Blackjack, Pass the Pig, Hangman, Anagram, Go Fish, War, Uno, Connect 4\n')
    
    if pick_players:
        while True:
            try:
                numPlayers = int(input("How many people are playing? "))
            except: 
                print('Please enter a valid number')
            else:
                if numPlayers > 6 or numPlayers < 2:
                    print('Please enter a valid number')
                else:
                    break
        player1 = Player(name_player('Player 1'))
        players = [player1]
        if numPlayers > 1:
            player2 = Player(name_player('Player 2'))
            players.append(player2)
            if numPlayers > 2:
                player3 = Player(name_player('Player 3'))
                players.append(player3)
                if numPlayers > 3:
                    player4 = Player(name_player('Player 4'))
                    players.append(player4)
                    if numPlayers > 4:
                        player5 = Player(name_player('Player 5'))
                        players.append(player5)
                        if numPlayers > 5:
                            player6 = Player(name_player('Player 6'))
                            players.append(player6)
    
    while board.done != True:
        board.print_board()
        current = players[turn % numPlayers]
        
        first_card = ask_card(current.name, board)
        second_card = ask_card(current.name, board)
        
        first_card.hidden = False
        second_card.hidden = False
        
        board.print_board()
        
        if first_card.value == second_card.value:
            print("CORRECT! {}, +1 point.\n".format(current.name))
            first_card.done = False
            second_card.done = False
            board.doneCards += 2
            current.score += 1
        else:
            first_card.hidden = True
            second_card.hidden = True
            print("INCORRECT.\n")
        
        if board.doneCards == 64:
            break
        
        os.system('cls')
        
        turn += 1
    
    print("GAME OVER.\n")
    
    winner = Player('Winner')
    winners = []
    
    for player in players:
        print(player)
        if player.score > winner.score:
            winner = player
            winners = [player]
        elif player.score == winner.score:
            winners.append(player)
        
    if len(winners) == 1:
        print("\nCONGRADULATIONS, {}.\n".format(winner.name))
    else:
        print("TIE GAME, CONGRADULATIONS TO ", end = "")
        for win in winners:
            if winners[-1] != win:
                print(win.name, end = ", ")
            else:
                print(win.name, end = ".\n")
    
    play_again = input("Would you like to play again? >> ")
    if 'y' in play_again:
        pick = input("Would you like to repick the players? >> ")
        if 'y' in pick:
            memoryflip(False, True)
        else:
            memoryflip(False, False)
            
memoryflip()