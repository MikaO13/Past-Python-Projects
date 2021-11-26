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
        self.fours = [] #how many fours there are in a hand
        self.name = name
    
    def add_card(self,card):
        #Card passed in from Deck.deal()
        self.cards.append(card)
    
    def check_four(self):
        for rank in ranks:
            count = []
            for card in self.cards:
                if card.rank == rank:
                    count.append(card)
            if len(count) == 4:
                for card in count:
                    self.cards.remove(card)
                self.fours.append(rank)
                print('\n' + self.name.upper() + 'HAS COMPLETED A SET OF FOUR WITH ' + rank.upper() + 'S!\n')
            else:
                count = []
            
    def fin(self):
        print(self.name.upper() + "'S SETS OF FOURS\n")
        if len(self.fours) > 0:
            for four in self.fours:
                print(four)
        else:
            print("FISHING FAILURE\n")
            
    def sort(self):
        newlist = []
        while self.cards != []:
            greatest = 0
            greatcard = None
            for card in self.cards:
                value = values[card.rank]
                if value > greatest:
                    greatest = value
                    greatcard = card
            newlist.append(greatcard)
            self.cards.remove(greatcard)
        self.cards = newlist
    
    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n' + card.__str__()
        return '\n' + self.name + "'s hand consists of " + hand_comp + '\n'
def showcards(numPlayers, player,player1,player2,player3,player4):
    print(player,end='\n')
    if player != player1:
        print(player1.name + ' has ' + str(len(player1.cards)) + ' cards.\n')
    if player != player2:
        print(player2.name + ' has ' + str(len(player2.cards)) + ' cards.\n')
    if numPlayers > 2 and player != player3:
        print(player3.name + ' has ' + str(len(player3.cards)) + ' cards.\n')
    if numPlayers > 3 and player != player4:
        print(player4.name + ' has ' + str(len(player4.cards)) + ' cards.\n')
def fishing(player1,player2,rank,deck):
    count = 0
    for card in player2.cards:
        if card.rank == rank:
            player1.cards.append(card)
            player2.cards.remove(card)
            player1.sort()
            count += 1
    if count > 0:
        print('\n' + player1.name + ' has fished ' + str(count) + ' ' + rank + '(s) from ' + player2.name)
        return True
    else: 
        player1.cards.append(deck.deal())
        player1.sort()
        return False
def askingfish(player,players,player1,player2,player3,player4,numPlayers):
    if numPlayers == 2:
        if player == player1:
            fishperson = player2
        elif player == player2:
            fishperson = player1
            
    else:
        while True:
            fish = input("Who would you like to 'fish' from, " + player.name + '? ')
            if fish == player.name or fish not in players:
                print('Please enter a valid player')
            else:
                if fish == player1.name:
                    fishperson = player1
                elif fish == player2.name:
                    fishperson = player2
                elif fish == player3.name:
                    fishperson = player3
                elif fish == player4.name:
                    fishperson = player4
                break
    return fishperson
def askingrank(player):
    while True:
        rank = input("What card rank would you like to steal? ")
        rank.capitalize()
        rankin = False
        for card in player:
            if card.rank == rank:
                rankin = True
        if rank not in ranks or rankin:
            print('Please enter a valid rank')
        else:
            return rank
            break
while True:
    deck = Deck()
    deck.shuffle()
    order = 1
    print("Hello and Welcome to Mika's Go Fish Game!")
    print('Other games by Mika: Blackjack, Roll the Pig, Hangman\n')
    print('Players start with 7 cards each, with minimum 2 and maximum 4 players.\nThe objective of the game is to get the most sets of 4 cards, like 4 Aces.')
    print("During their turn, a player can choose another player to go 'fishing' from.")
    print("While 'fishing', a player picks a certain rank (ex: ace),\nand if the player they chose has one or more of that rank,")
    print("that player gives all their cards of that rank to the player 'fishing'.\nIf not, the player 'fishing' draws a card from the deck.\n\n")
    
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
    for player in range(1,numPlayers+1):
        if player == 1:
            current = player1
        elif player == 2:
            current = player2
        elif player == 3:
            current = player3
        elif player == 4:
            current = player4
        for i in range(1,8):
            current.add_card(deck.deal())
        for player in players:
            player.sort()
    while len(deck.deck) > 0:
        if order % numPlayers == 1:
            active = player1
        elif order % numPlayers == 2:
            active = player2
        elif order % numPlayers == 3:
            active = player3
        elif order % numPlayers == 0:
            if numPlayers == 2:
                active = player2
            elif numPlayers == 3:
                active = player3
            elif numPlayers == 4:
                active = player4
        fishy = True
        print('\n' + active.name.upper() + "'S TURN")
        quit = input("Would you like to quit the game? ")
        if 'yes' in quit:
            deck.deck = []
            fishy = False
        while fishy:
            showcards(numPlayers,active,player1,player2,player3,player4)
            fish = askingfish(active,players,player1,player2,player3,player4,numPlayers)
            rank = askingrank(active)
            fishy = fishing(active,fish,rank,deck)
            active.check_four()
            if fishy:
                print('Go again, ' + active.name)
            else:
                print("Go fish, " + active.name + ", your turn is over.")
                break
        order += 1
      
    print("\nSETS OF FOUR")
    player1.fin()
    player2.fin()
    if numPlayers > 2:
        player3.fin()
        if numPlayers > 3:
            player4.fin()
            
    # check who wins
    if len(player1.fours) > len(player2.fours):
        winner = [player1]
        highest = len(player1.fours)
    elif len(player1.fours) < len(player2.fours):
        winner = [player2]
        highest = len(player2.fours)
    else:
        winner = [player1,player2]
        highest = len(player1.fours)
    if numPlayers > 2:
        if len(player3.fours) > highest:
            winner = [player3]
        elif len(player3.fours) == highest:
            winner.append(player3)
        if numPlayers > 3:
            if len(player4.fours) > highest:
                winner = [player4]
            elif len(player4.fours) == highest:
                winner.append(player4)
                
    if len(winner) == numPlayers:
        print("\nTIE GAME")
    elif len(winner) != numPlayers and len(winner) > 1:
        print("\nTIE WIN; ",end="")
        count = 0
        for person in winner:
            print(person.name.upper,end="")
            if count + 1 == len(winner):
                print(" and ",end="")
            count += 1
        print(" WIN!")
    elif len(winner) == 1:
        print(winner[0].name.upper() + " WINS!")
    
    new_game = input("\nWould you like to play another hand? ")
    if 'yes' in new_game.lower():
        deck = Deck()
        continue
    else:
        print("Please come visit us at Mika's Go Fish Game (or another of Mika's games) again soon!")
        break

