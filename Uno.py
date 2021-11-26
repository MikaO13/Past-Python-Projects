'''
Ideas

turn color of card to color of card - works except special rainbow
fix to ignore errors (try/except/else)
make so draw 2 and wild draw 4 can be multiple words instead of one squished
'''

import random
from colorama import init
from termcolor import colored
colors = ('Red', 'Blue', 'Yellow', 'Green', 'Special')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'One', 'Reverse', 'Skip', 'Draw2', 'Wild', 'WildDraw4', 'Zero')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'One':1, 'Reverse':11, 'Skip':12, 'Draw2':13, 'Wild':14, 'WildDraw4':15, 'Zero':0}
col = {'Red':'red', 'Blue':'blue', 'Yellow':'yellow', 'Green':'green', 'Special':'magenta'} # change later to rainbow colors

class Card:
    
    def __init__(self,color,rank):
        self.color = color
        self.rank = rank
    
    def __str__(self):
        pricolor = col[self.color]
        return colored(self.color,pricolor) + ' ' + colored(self.rank,pricolor)

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for color in colors[:3]:
            for rank in ranks[:13]:
                self.deck.append(Card(color,rank))
                self.deck.append(Card(color,rank))
            self.deck.append(Card(color,'Zero'))
        for special in range(4):
            self.deck.append(Card('Special', 'Wild'))
            self.deck.append(Card('Special', 'Wilddraw4'))
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self,name):
        self.cards = []
        self.name = name
    
    def add_card(self,card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            if card != self.cards[-1]:
                hand_comp += card.__str__() + ', '
            else:
                hand_comp += card.__str__() + '.'
        return self.name + ' has: ' + hand_comp
    
    def sort(self):
        cardsorted = []
        for color in colors:
            colorlst = []
            for card in self.cards:
                if card.color == color:
                    colorlst.append(card)
            for rnd in range(len(colorlst)-1):
                for bubble in range(len(colorlst)-1-rnd):
                    first = colorlst[bubble]
                    second = colorlst[bubble+1]
                    if values[first.rank] > values[second.rank]:
                        colorlst[bubble] = second
                        colorlst[bubble+1] = first
            for item in colorlst:
                cardsorted.append(item)
        self.cards = cardsorted
    
def play_card(player, prev, deck):
    match = False
    picking = True
    for card in player.cards:
        if card.color == prev.color or card.rank == prev.rank or card.color == 'Special':
            match = True
            break
    print(player)
    if match:
        while picking:
            print('The last card played was ' + colored(prev.color,col[prev.color]) + ' ' + colored(prev.rank,col[prev.color]))
            card = input(player.name + ', what card would you like to play? ')
            card = card.split()
            try:
                newcard = Card(str(card[0]).capitalize(),str(card[1]).capitalize())
            except:
                continue
            else:
                cardin = False
                for card in player.cards:
                    if newcard.color == card.color and newcard.rank == card.rank:
                        cardin = True
                        picked = card
                if newcard.color in colors and newcard.rank in ranks and cardin and (newcard.color == prev.color or newcard.rank == prev.rank or newcard.color == 'Special'):
                    picking = False
                else:
                    print('\nPlease remember to enter a valid input in the form of Color Rank')
        player.cards.remove(picked)
        return newcard
    else:
        print(player.name + ' cannot play a card. DRAW CARD\n')
        player.add_card(deck.deal())
        return prev

def check_win(players):
    win = False
    for player in players:
        if len(player.cards) == 0:
            win = True
            return player
    return win

while True:
    
    deck = Deck()
    deck.shuffle()
    turn = 0
    prev = deck.deal()
    placed = [prev]
    change = 1
    while prev == 'Special':
        prev = deck.deal()
        placed.append(prev)
    first_time = True
    if first_time:
        print("Hello and Welcome to Mika's Uno Game!")
        print('Other games by Mika: Blackjack, Pass the Pig, Hangman, Anagram, Go Fish, War\n')
        if 'y' in input('Would you like to hear the rules? ').lower():
            print('Each player starts with 7 cards, with max 6 players.'
                  '\nTypes of Cards: 0-10, Reverse, Draw2, Wild, WildDraw4'
                  "\n0-10 are regular cards, Reverse reverses the direction of the players (ex: counterclockwise instead of clockwise), Skip skips the next players' turn,"
                  '\nDraw 2 makes the next player draw two cards, Wild changes the color, and Wild Draw 4 changes the color and makes the next player draw 4 cards'
                  "\nOn a player's turn, they attempt to put down a card either matching color or matching rank (ex: matching 6s or matching blue)"
                  '\nA player inputs a card by typing Color Rank (ex: Blue 4). Wild and Wild Draw 4 have the color Special'
                  '\nIf a player does not have a card to put down, they continue drawing cards until they have one to play, and the turn passes to the next player'
                  '\nIf a player places the same card as the previous card, they get to go again. '
                  '\nThe goal of the game is to get rid of all your cards before your opponents.'
                  '\nNow that you know the rules, let us get started!\n')
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
        forbiddenames = []
        name1 = input("What would you like to be called, Player 1? ")
        if name1 in forbiddenames:
            name1 == "Player 1"
        forbiddenames.append(name1)
        name2 = input("What would you like to be called, Player 2? ")
        if name2 in forbiddenames:
            name2 == "Player 2"
        forbiddenames.append(name2)
        if numPlayers > 2:
            name3 = input("What would you like to be called, Player 3? ")
            if name3 in forbiddenames:
                name3 == "Player 3"
            forbiddenames.append(name3)
            if numPlayers > 3:
                name4 = input("What would you like to be called, Player 4? ")
                if name4 in forbiddenames:
                    name4 == "Player 4"
                forbiddenames.append(name4)
                if numPlayers > 4:
                    name5 = input("What would you like to be called, Player 5? ")
                    if name5 in forbiddenames:
                        name5 == "Player 5"
                    forbiddenames.append(name5)
                    if numPlayers > 5:
                        name6 = input("What would you like to be called, Player 6? ")
                        if name6 in forbiddenames:
                            name6 == "Player 6"
                        forbiddenames.append(name6)
        player1 = Hand(name1)
        player2 = Hand(name2)
        players = [player1,player2]
        if numPlayers > 2:
            player3 = Hand(name3)
            players.append(player3)
            if numPlayers > 3:
                player4 = Hand(name4)
                players.append(player4)
                if numPlayers > 4:
                    player5 = Hand(name5)
                    players.append(player5)
                    if numPlayers > 5:
                        player6 = Hand(name6)
                        players.append(player6)
    for player in players:
        for card in range(7):
            player.add_card(deck.deal())
    for player in players:
        player.sort()
    while check_win(players) == False:
        current = players[(turn % numPlayers)]
        nxt = players[((turn + change) % numPlayers)]
        turn += change
        print('\nOrder of players: ')
        for player in players:
            if player != players[-1]:
                print(player.name,end=', ')
            else:
                print(player.name,end='.\n\n')
        new_prev = play_card(current,prev,deck)
        placed.append(new_prev) # this code is for drawing cards until place card
        while new_prev == prev:
            prev = new_prev
            current.sort()
            new_prev = play_card(current,prev,deck)
            placed.append(new_prev)
        prev = new_prev
        current.sort()
        # do special card things (reverse, +2, skip, wild, wild +4)
        if prev.rank == 'Skip':
            print(nxt.name + "'s turn has been skipped.")
            turn += 1
        elif prev.rank == 'Reverse':
            change *= -1
            # make it so that it starts with current and then loops around to end with the one before current?
            print('The order of play has been reversed.')
        elif prev.rank == 'Draw2':
            print(nxt.name + ' has to draw two cards.')
            nxt.add_card(deck.deal())
            nxt.add_card(deck.deal())
            nxt.sort()
        elif prev.rank == 'Wild':
            while True:
                color = input('What would you like to change the color to, ' + current.name + '? ').capitalize()
                if color in colors and color != 'Special':
                    prev.color = color
                    break
        elif prev.rank == 'WildDraw4':
            print(nxt.name + ' has to draw four cards.')
            for card in range(4):
                nxt.add_card(deck.deal())
            nxt.sort()
            while True:
                color = input('What would you like to change the color to, ' + current.name + '? ').capitalize()
                if color in colors and color != 'Special':
                    prev.color = color
                    break
        for player in players:
            if len(player.cards) == 1:
                print(player.name + ' UNO!')
        if len(deck.deck) <= 10:
            deck.shuffle()
    
    print(player.name.upper() + ' WINS!\n')
    new_game = input("\nWould you like to play another game? ")
    if 'y' in new_game.lower():
        first_time = False
        continue
    else:
        print("Please come visit us at Mika's Uno Game again soon!")
        break