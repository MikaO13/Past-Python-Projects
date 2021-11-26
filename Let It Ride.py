import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':1, 'Three':2, 'Four':3, 'Five':4, 'Six':5, 'Seven':6, 'Eight':7, 'Nine':8, 'Ten':9, 'Jack':10, 'Queen':11, 'King':12, 'Ace':13}
winningHands = {"Royal Flush":1000, "Straight Flush":200, "Four of a Kind":50, "Full House":11, "Flush":8, "Straight":5, "Three of a Kind":3, "Two Pair":2, "Pair 10+":1}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank+' of '+self.suit

class Deck:
    
    def __init__(self):
        self.deck = [] 
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
        self.smallHand = []
        self.fullHand = []
        self.winningType = ""
        self.name = name
        self.chips = chips
    
    def add_card(self,card,community):
        if community == False:
            self.smallHand.append(card)
        self.fullHand.append(card)
            
    def sort(self, hand):
        newlist = []
        while hand != []:
            greatest = 0
            greatcard = None
            for card in hand:
                value = values[card.rank]
                if value > greatest:
                    greatest = value
                    greatcard = card
            newlist.append(greatcard)
            hand.remove(greatcard)
        return newlist
    
    def take_bet(self):
        while True:
            try:
                amt = int(input('\n' + self.name + ", how much would you like to bet? >> "))
            except:
                print("Please enter a valid amount.")
                continue
            else:
                if self.chips.total < amt or amt <= 0:
                    print("Please enter a valid amount.")
                else:
                    return amt
                    
    def pull_or_ride(self):
        while True:
            choice = input("\n{}, would you like to pull a pet or 'let it ride'? >>".format(self.name))
            if 'pull' in choice:
                choice = 'pull'
                break
            elif 'ride' in choice:
                choice = 'ride'
                break
            else:
                print("Please enter a valid choice.")
                continue
        return choice
    
    def __str__(self):
        hand_comp = ''
        for card in self.smallHand:
            if card != self.smallHand[-1]:
                hand_comp += card.__str__() + ', '
            else:
                hand_comp += card.__str__() + '.'
        return "{} has: {}".format(self.name, hand_comp)

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        self.numBets = 0
        
    def win_bet(self, winType):
        self.total += self.numBets * self.bet * winningHands[winType]
    
    def lose_bet(self):
        self.total -= self.bet * self.numBets

def royal_flush(hand):
    winning = straight_flush(hand)
    if winning:
        card_nums = count_cards(hand)
        if 'Ten' in card_nums and 'Jack' in card_nums and 'Queen' in card_nums and 'King' in card_nums and 'Ace' in card_nums:
            return winning
        else:
            return False
        
def straight_flush(hand): 
    winning = flush(hand)
    if winning:
        suit = winning[0].suit
        
    flush_hand = []
    
    for card in hand:
        if card.suit == suit:
            flush_hand.append(card)
    
    return straight(flush_hand)
        
def four(hand):
    card_nums = count_cards(hand)
    four_value = 0
    for value in card_nums:
        if card_nums[value] >= 4:
            four_value = value
    if four_value != 0:
        cards = []
        for card in hand:
            if card.rank == four_value and len(cards) < 4:
                cards.append(card)
        return cards
    return False

def full_house(hand): 
    card_nums = count_cards(hand)
    pair_value = 0
    three_value = 0
    for value in card_nums:
        if card_nums[value] >= 3 and three_value == 0:
            three_value = value
    for value in card_nums:
        if card_nums[value] >= 2 and value != three_value:
            pair_value = value
    if pair_value != 0 and three_value != 0:
        full_cards = []
        for card in hand:
            if card.rank == pair_value and len(full_cards) < 2:
                full_cards.append(card)
        for card in hand:
            if card.rank == three_value and len(full_cards) < 5:
                full_cards.append(card)
        return full_cards
    else:
        return False

def flush(hand):
    card_suits = {}
    for card in hand:
        if card.suit in card_suits:
            card_suits[card.suit] += 1
        else:
            card_suits[card.suit] = 1
    flush_suit = None
    for suit in card_suits:
        if card_suits[suit] >= 5:
            flush_suit = suit
    if flush_suit != None:
        flush_cards = []
        for card in hand:
            if card.suit == flush_suit and len(flush_cards) < 5:
                flush_cards.append(card)
        return flush_cards
    else:
        return False
            
def straight(hand):
    card_nums = []
    for card in hand:
        if values[card.rank] not in card_nums:
            card_nums.append(values[card.rank])
    great_start_card = 0
    
    for value in card_nums:
        if ((value)% 13)+1 in card_nums and ((value+1)% 13)+1 in card_nums and ((value+2)% 13)+1 in card_nums and ((value+3)% 13)+1 in card_nums:
            if value > great_start_card:
                great_start_card = value
    
    if great_start_card != 0:
        straight_cards = []
        winning_ranks = [great_start_card, ((great_start_card)% 13)+1,
                         ((great_start_card+1)% 13)+1, ((great_start_card+2)% 13)+1, 
                         ((great_start_card+3)% 13)+1]
        for card in hand:
            if values[card.rank] in winning_ranks:
                straight_cards.append(card)
                winning_ranks.remove(values[card.rank])
                
        return straight_cards
    else:
        return False

def three(hand): 
    card_nums = count_cards(hand)
    three_value = 0
    for value in card_nums:
        if card_nums[value] >= 3 and value > three_value:
            three_value = value
    if three_value != 0:
        cards = []
        for card in hand:
            if card.rank == three_value and len(cards) < 3:
                cards.append(card)
        return cards
    else:
        return False
        
def two_pair(hand):
    card_nums = count_cards(hand)
    pair_values = []
    for value in card_nums:
        if card_nums[value] >= 2:
            if value not in pair_values:
                pair_values.append(value)
    if len(pair_values) == 2:
        pair_cards = []
        for value in pair_values:
            for card in hand:
                if card.rank == value and len(pair_cards) < 2*(pair_values.index(value) + 1):
                    pair_cards.append(card)
        return pair_cards
    else:
        return False

def pair_10_plus(hand): 
    card_nums = count_cards(hand)
    pair_value = 0
    for value in card_nums:
        if card_nums[value] >= 2 and value >= 10:
            pair_value = value
    if pair_value != 0:
        pair_cards = []
        for card in hand:
            if card.rank == pair_value and len(pair_cards) < 2:
                pair_cards.append(card)
        return pair_cards
    else:
        return False

def count_cards(hand):
    card_nums = {}
    for card in hand:
        if card.rank in card_nums:
            card_nums[card.rank] += 1
        else:
            card_nums[card.rank] = 1
    return card_nums

def check_win(hand):
    best_hand = []
    best_type = ""
    comparing = royal_flush(hand)
    if comparing:
        best_hand = comparing
        best_type = "Royal Flush"
    else:
        comparing = straight_flush(hand)
        if comparing:
            best_hand = comparing
            best_type = "Straight Flush"
        else:
            comparing = four(hand)
            if comparing:
                best_hand = comparing
                best_type = "Four of a Kind"
            else:
                comparing = full_house(hand)
                if comparing:
                    best_hand = comparing
                    best_type = "Full House"
                else:
                    comparing = flush(hand)
                    if comparing:
                        best_hand = comparing
                        best_type = "Flush"
                    else:
                        comparing = straight(hand)
                        if comparing:
                            best_hand = comparing
                            best_type = "Straight"
                        else:
                            comparing = three(hand)
                            if comparing:
                                best_hand = comparing
                                best_type = "Three of a Kind"
                            else:
                                comparing = two_pair(hand)
                                if comparing:
                                    best_hand = comparing
                                    best_type = "Two Pair"
                                else:
                                    comparing = pair_10_plus(hand)
                                    if comparing:
                                        best_hand = comparing
                                        best_type = "Pair 10+"
                                    else:
                                        best_hand, best_type = None, None
    return best_hand, best_type

def name_player(default):
    global forbiddenames
    name = input("What would you like to be called? >> ")
    if name in forbiddenames:
        name == default
    forbiddenames.append(name)
    return name

def printCommunityCards(communityCards):
    print("The community cards are: ")
    for card in communityCards:
        if communityCards[len(communityCards) - 1] != card:
            print(card, end = ", ")
        else:
            print(card, end = ".\n\n")

def letitride(first_time=True, pick_players=True):
    global forbiddenames

    forbiddenames = []
    communityCards = []
    
    deck = Deck()
    deck.shuffle()
    
    if first_time:
        print("Hello and Welcome to Mika's Let It Ride Table!")
        print('Other games by Mika: Texas Hold Em, Blackjack, Pass the Pig, Hangman, Anagram, Go Fish, War, Uno, Connect 4\n')
        if 'y' in input('Would you like to hear the rules? ').lower():
            print('This game is a variation of the classic betting card game, poker.'
                  '\nAt this table, there are max 6 players.'
                  '\nI am referring you to this website - https://wizardofodds.com/games/let-it-ride/ - to learn the rules.'
                  '\nNow that you know the rules, let us get started!\n')
    
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
        player1 = Hand(name_player('Player 1'),Chips())
        players = [player1]
        if numPlayers > 1:
            player2 = Hand(name_player('Player 2'),Chips())
            players.append(player2)
            if numPlayers > 2:
                player3 = Hand(name_player('Player 3'),Chips())
                players.append(player3)
                if numPlayers > 3:
                    player4 = Hand(name_player('Player 4'),Chips())
                    players.append(player4)
                    if numPlayers > 4:
                        player5 = Hand(name_player('Player 5'),Chips())
                        players.append(player5)
                        if numPlayers > 5:
                            player6 = Hand(name_player('Player 6'),Chips())
                            players.append(player6)
                            
    for player in players:
        player.chips.bet = player.take_bet()
        
    for player in players:
        for card in range(3):
            player.add_card(deck.deal(), False)
        player.smallHand = player.sort(player.smallHand)
        player.fullHand = player.smallHand
    
    for rnd in range(2):
        for player in players:
            choice = player.pull_or_ride()
            if choice == 'pull':
                player.chips.numBets -= 1
            elif choice == 'ride':
                continue
            print("{} has {} bets of {} chips left.\n".format(player.name, str(player.numBets), str(player.bet)))
        
        rndcard = deck.deal()
        communityCards.append(rndcard)
        for player in players:
            player.add_card(rndcard, True)
            player.sort(player.fullHand)
        printCommunityCards(communityCards)
    
    for player in players:
        player.winningHand, player.winningType = check_win(player.fullHand)
        winningCards = ""
        for card in player.winningHand:
            winningCards += card.rank +' of '+ card.suit
            if player.winningHand.index(card) != len(player.winningHand) - 1:
                winningCards += ", "
            else:
                winningCards += "."
                
        print("{} has a {}, with cards {}.".format(player.name, player.winningType, winningCards))
        if player.winningType in winningHands:
            print("With a {} bet(s) of {}, {} earns {} chips.".format(str(player.chips.numBets), str(player.chips.bet), player.name, str(player.chips.numBets * player.chips.bet * winningHands[player.winningType])))
            player.chips.win_bet(player.winningType)
        else:
            print("With a {} bet(s) of {}, {} loses {} chips.".format(str(player.chips.numBets), str(player.chips.bet), player.name, str(player.chips.bet)))
            player.chips.lose_bet()
                           
    play_again = input("Would you like to play another hand? >> ")
    if 'y' in play_again.lower():
        repick_players = input("Would you like to repick the players at the table? >> ")
        if 'y' in repick_players.lower():
            letitride(False, True)
        else:
            letitride(False, False)
    else:
        print("Thank you for playing at Mika's Let It Ride Table!\nPlease play again and tell your friends!")
    