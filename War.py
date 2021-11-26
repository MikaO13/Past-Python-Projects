import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':1}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank+' of '+self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self,name):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.name = name
        self.card = None
    
    def add_card(self,card):
        #Card passed in from Deck.deal()
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

def compare_cards(card1,card2):
    if values[card1.rank] > values[card2.rank]:
        return True
    else:
        return False

def print_cards(players):
    print('Cards Battling:')
    for player in players:
        print(player.name,end="")
        print(': ',end="")
        print(player.card)

while True:
    deck = Deck()
    deck.shuffle()
    first_time = True
    if first_time:
        print("Hello and Welcome to Mika's Game of War!")
        print('Other games by Mika: Blackjack, Roll the Pig, Hangman, Anagram, Go Fish\n')
        if 'y' in input('Would you like to hear the rules? ').lower():
            print('The deck is split equally between the players.'
                  '\nEach round, all players place down a card, and the player with the highest value card gets all the cards.'
                  '\nAfter 20 rounds the person with the most cards wins. This is to ensure the game does not go on forever.'
                  '\nNow that you know the rules, let us get started!\n')
        while True:
            try:
                numPlayers = int(input("How many people are playing? "))
            except: 
                print('Please enter a valid number')
            else:
                if numPlayers > 4 or numPlayers < 2:
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
        player1 = Hand(name1)
        player2 = Hand(name2)
        players = [player1,player2]
        if numPlayers > 2:
            player3 = Hand(name3)
            players.append(player3)
            if numPlayers > 3:
                player4 = Hand(name4)
                players.append(player4)
    for player in players:
        for card in range(52//numPlayers):
            player.add_card(deck.deal())
    while len(players) > 1:
        print('\nNEW ROUND!\n')
        winning = Hand('throwaway')
        winning.card=Card('Hearts','Ace')
        for player in players:
            player.card = player.cards.pop()
            if compare_cards(player.card,winning.card):
                winning = player
        print_cards(players)
        print(winning.name + ' wins this round!')
        for player in players:
            winning.add_card(player.card)
            if len(player.cards) == 0:
                players.remove(player)
            player.shuffle()
        rnd += 1
    new_game = input("\nWould you like to play another game? ")
    if 'y' in new_game.lower():
        deck = Deck()
        for player in players:
            player.cards = []
        continue
    else:
        print("Please come visit us at Mika's Game of War (or another of Mika's games) again soon!")
        break
