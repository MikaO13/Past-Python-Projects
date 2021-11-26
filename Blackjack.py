import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

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
    def __init__(self,name,chips):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.name = name
        self.chips = chips
    
    def add_card(self,card):
        #Card passed in from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]
        
        #track aces
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
    def blackjack(self):
        self.total += self.bet*2.5

def take_bet(player):
    while True:
        try:
            amt = int(input('\n' + player.name + ", how much would you like to bet? "))
        except:
            print("Please enter a valid amount.")
            continue
        else:
            if player.chips.total < amt or amt <= 0:
                print("Please enter a valid amount.")
            else:
                return amt
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    action = input('\n' + hand.name + ', would you like to hit or stand? ')
    check = True
    while check:
        if action.lower() == 'hit':
            hit(deck,hand)
            check = False
        elif action.lower() == 'stand':
            print(hand.name + " Stands, Dealer Turn")
            playing = False
            check = False
        else:
            print('Please enter hit or stand ONLY.')
            action = input('Would you like to hit or stand? ')

def turn(deck,player,dealer):
    global playing
    print('\n' + player.name.upper() + "'S TURN")
    while playing:
        hit_or_stand(deck,player)
        if playing:
            showcards(players,dealer,'some')
        if player.value > 21:
            player_busts(player,dealer)
            playing = False

def show(player):
    player_total = 0
    print("\n" + player.name.upper() +" HAND:")
    for card in player.cards:
        print(' ', end='')
        print(card)
        player_total += values[card.rank]
    print(player.name + ' Total: ' + str(player_total))

def dealershow(dealer,amt):
    dealer_total = 0
    print('\nDEALER HAND:\n')
    if amt == 'some':
        print(" <hidden card>")
        print(' ', end='')
        print(dealer.cards[1])
        dealer_total += values[dealer.cards[1].rank]
        print('Dealer Total: ' + str(dealer_total) + ' + ?')
    elif amt == 'all':
        for card in dealer.cards:
            print(' ', end='')
            print(card)
            dealer_total += values[card.rank]
        print('Dealer Total: ' + str(dealer_total))
                        
def showcards(players,dealer,amt):
    dealershow(dealer,amt)
    
    for player in players:
        show(player)
                        
def what_blackjack(hand):
    color = ''
    typecard = ''
    special = None
    for card in hand.cards:
        if values[card.rank] == 10:
            special = card
    typecard = special.rank
    if special.suit == 'Hearts' or special.suit == 'Diamonds':
        color = 'Red'
    else:
        color = 'Black'
    print('You have a ' + color + ' ' + typecard + '!')
    if color == 'Black' and typecard == 'Jack':
        print(hand.name.upper() +' HAS A REAL BLACKJACK, CONGRADULATIONS!')
        print('A TRUE blackjack, with an ace and a black (spades or clubs) jack')
        print('has the odds of 4/663, or about 0.00603318, which amounts to practically NEVER.')
        print("All of the players here today are lucky to get to witness a TRUE blackjack on Mika's Blackjack Table!\n")
def player_busts(player,dealer):
    print('\nBUST PLAYER!\n' + player.name.upper() + ' LOSE!')
    player.chips.lose_bet()
    
def player_wins(player,dealer):
    print('\n' + player.name.upper() + ' WINS!')
    player.chips.win_bet()

def dealer_busts(player,dealer):
    print('\nBUST DEALER!\n' + player.name.upper() + ' WINS!')
    player.chips.win_bet()
    
def dealer_wins(player,dealer):
    print('\nDEALER WINS!\n' + player.name.upper() + ' LOSE!')
    player.chips.lose_bet()
    
def push(player,dealer):
    print('\nDealer and ' + player.name + ' tie!\nPUSH!')

def player_blackjack(player,dealer):
    print('\nPLAYER BLACKJACK\n' + player.name.upper() + ' WINS 2.5x BET!')
    what_blackjack(player)
    player.chips.blackjack()

def dealer_blackjack(player,dealer):
    print('\nDEALER BLACKJACK!\n' + player.name.upper() + ' LOSE!')
    what_blackjack(dealer,'dealer')
    player.chips.lose_bet()

def endscenarios(player,dealer):
    if player.value <= 21:
        # Run different winning scenarios
        if player.value > dealer.value:
            player_wins(player,dealer)
        elif dealer.value > 21:
            dealer_busts(player,dealer)
        elif dealer.value > player.value:
            dealer_wins(player,dealer)
        elif dealer.value == player.value:
            push(player,dealer)

playing = True
first_time = True
noblackjack = True

'''
MAKE NAME AND STUFF A PART OF HAND 
'''

while True:
    # Print an opening statement
    if first_time:
        print("Hello and welcome to Mika's Blackjack Table!\n")
        print("Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.")
        print("21 on first deal is Blackjack, meaning an automatic win!\n")
        print("Minimum 1 player at this table, maximum 6.")
        while True:
            try:
                numPlayers = int(input("How many people are playing? "))
            except:
                print("Please enter a valid amount.")
            else:
                if numPlayers <= 0 or numPlayers > 6: 
                    print("Please enter a valid amount.")
                else:
                    break
        deck = Deck()
        forbiddenames = [" ", ""]
        name1 = input("What would you like to be called, Player 1? ")
        if name1 in forbiddenames:
            name1 == "Player 1"
        forbiddenames.append(name1)
        if numPlayers > 1:
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
        player1 = Hand(name1,Chips())
        players = [player1]
        if numPlayers >= 2:
            player2 = Hand(name2,Chips())
            players.append(player2)

            if numPlayers >= 3:
                player3 = Hand(name3,Chips())
                players.append(player3)

                if numPlayers >= 4:
                    player4 = Hand(name4,Chips())
                    players.append(player4)

                    if numPlayers >= 5:
                        player5 = Hand(name5,Chips())
                        players.append(player5)

                        if numPlayers == 6:
                            player2 = Hand(name6,Chips())
                            players.append(player6)
        dealer = Hand('Dealer',0)
        first_time = False
    # Create & shuffle the deck, deal two cards to each player
    deck.shuffle()
    hit(deck,dealer)
    hit(deck,dealer)
    dealer.adjust_for_ace()
    for player in players:
        hit(deck,player)
        hit(deck,player)
        player.adjust_for_ace()
        player.chips.bet = take_bet(player)
        
    print('\nCHIPS COUNT')
    for player in players:
        print(player.name + ': ' + str(player.chips.total))
    
    # Show cards (but keep one dealer card hidden)
    showcards(players,dealer,'some')
    
    for player in players:
        if player.value == 21:
            player_blackjack(player,dealer)
        else:
            playing = True
            turn(deck,players,dealer)

    #check for dealer's blackjack
    if dealer.value == 21:
        for player in players:
            dealer_blackjack(player,dealer)
        noblackjack=False
        
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    
    while dealer.value < 17 and noblackjack:
        print('\nDealer Hit')
        showcards(players,dealer,'all')
        hit(deck,dealer)
        # Show all cards
    print('\nDealer Stand')
    showcards(players,dealer,'all')
    
    for player in players:
        if player.value < 21:
            endscenarios(player,dealer)
    # Inform Player of their chips total 
    print('\nCHIPS COUNT')
    for player in players:
        print(player.name + ': ' + str(player.chips.total))
    
    # Ask to play again
    
    new_game = input("\nWould you like to play another hand? ")
    if 'yes' in new_game.lower():
        playing=True
        continue
    else:
        print("Please come visit us at Mika's Blackjack Table again soon!")
        break



