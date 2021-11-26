import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':1, 'Three':2, 'Four':3, 'Five':4, 'Six':5, 'Seven':6, 'Eight':7, 'Nine':8, 'Ten':9, 'Jack':10, 'Queen':11, 'King':12, 'Ace':13}
winningHands = {"Royal Flush":1, "Straight Flush":2, "Four of a Kind":3, "Full House":4, "Flush":5, "Straight":6, "Three of a Kind":7, "Two Pair":8, "One Pair":9, "High Card":10}

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
        self.winningHand = []
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
        self.roundBet = 0
        self.inRound = True
        
    def bet(self, amt):
        global pot
        global canCheck
        self.total -= amt
        pot += amt
        self.roundBet += amt
        canCheck = False

    def call(self):
        global currentBet
        amtToCall = currentBet-self.roundBet
        self.bet(amtToCall)
        
    def raise_bet(self, numRaise):
        global currentBet
        currentBet += numRaise
        self.bet(numRaise)
    
    def win_pot(self):
        global pot
        self.total += pot

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

def one_pair(hand): 
    card_nums = count_cards(hand)
    pair_value = 0
    for value in card_nums:
        if card_nums[value] >= 2:
            pair_value = value
    if pair_value != 0:
        pair_cards = []
        for card in hand:
            if card.rank == pair_value and len(pair_cards) < 2:
                pair_cards.append(card)
        return pair_cards
    else:
        return False

def high_card(hand):
    card_nums = count_cards(hand)
    highest_value = 0
    for value in card_nums:
        if values[value] > highest_value:
            highest_value = values[value]
    for card in hand:
        if values[card.rank] == highest_value:
            return [card]
        

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
                                    comparing = one_pair(hand)
                                    if comparing:
                                        best_hand = comparing
                                        best_type = "One Pair"
                                    else:
                                        best_hand = high_card(hand)
                                        best_type = "High Card"
    return best_hand, best_type

def name_player(default):
    global forbiddenames
    name = input("What would you like to be called? >> ")
    if name in forbiddenames:
        name == default
    forbiddenames.append(name)
    return name

def take_bet(player, options):
    global currentBet
    
    while True:
        print("{}, your options for betting this turn are ".format(player.name), end = "")
        for option in options:
            if option != options[len(options)-1]:
                print(option, end = ", ")
            else:
                print(option, end = ".\n")
        print("The current bet is {} and you have bet {}.".format(currentBet, player.chips.roundBet))
        bet = input("What would you like to choose? >> ")
        if bet.lower() not in options:
            continue
        else:
            break
            
    compute_betting_options(player, bet.lower())

def compute_betting_options(player, bet):
    global donePlayers
    global numActivePlayers
    
    if bet == "check":
        print("{} will check.".format(player.name))
        donePlayers += 1
    elif bet == "call":
        print("{} will call.".format(player.name))
        donePlayers += 1
        player.chips.call()
    elif bet == "raise":
        print("{} will raise.".format(player.name))
        print("{} has {} chips remaining, the current bet is {}, and betting is in increments of 5.".format(player.name, player.chips.total, currentBet))
        while True:
            try:
                amt = int(input("How much would you like to raise? "))
            except:
                print("Please enter a valid amount.")
            else:
                if amt < 0 or amt % 5 != 0 or amt > player.chips.total:
                    print("Please enter a valid amount.")
                else:
                    break
        player.chips.raise_bet(amt)
        donePlayers = 1
    elif bet == "fold":
        print("{} will fold.".format(player.name))
        donePlayers += 1
        player.chips.inRound = False
        numActivePlayers -= 1

def bettingRound(players, currentPlayerCounter, numPlayers):
    global donePlayers
    global currentBet
    global startingBet
    global startingPlayer
    global numActivePlayers
    
    while True:
        currentPlayer = players[(startingPlayer + currentPlayerCounter) % numActivePlayers] #this might have an error b/c of ppl folding
        if numActivePlayers == 1:
            return currentPlayer
        print(currentPlayer)
        
        if currentPlayer.chips.inRound == True:
            if currentPlayer.chips.roundBet == startingBet or currentPlayer.chips.roundBet == currentBet:
                take_bet(currentPlayer, ["check", "raise", "fold"])
            else:
                take_bet(currentPlayer, ["call", "raise", "fold"])
        currentPlayerCounter += 1
        if donePlayers == numPlayers:
            break
    return False
            
def printCommunityCards(communityCards):
    print("The community cards are: ")
    for card in communityCards:
        if communityCards[len(communityCards) - 1] != card:
            print(card, end = ", ")
        else:
            print(card, end = ".\n\n")

def sevencardstud(first_time=True, pick_players=True):
    global forbiddenames
    global pot
    global currentBet
    global startingBet
    global canCheck
    global donePlayers
    global numActivePlayers
    global startingPlayer
    
    donePlayers = 0
    numActivePlayers = 0
    
    pot = 0

    forbiddenames = []
    communityCards = []
    
    deck = Deck()
    deck.shuffle()
    
    if first_time:
        startingPlayer = 0
        print("Hello and Welcome to Mika's Seven Card Stud Table!")
        print('Other games by Mika: Texas Hold Em, Let It Ride, Blackjack, Pass the Pig, Hangman, Anagram, Go Fish, War, Uno, Connect 4\n')
        if 'y' in input('Would you like to hear the rules? ').lower():
            print('This game is a variation of the classic betting card game, poker.'
                  '\nAt this table, there are max 6 players.'
                  '\nI will refer you to this website - https://www.cardplayer.com/rules-of-poker/how-to-play-poker/games/seven-card-stud - to learn the rules.'
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
        for card in range(3):
            player.add_card(deck.deal(), False)
        player.smallHand = player.sort(player.smallHand)
        player.fullHand = player.smallHand
    
    numActivePlayers = numPlayers
    
    for rnd in ['begin','flop','turn','river']:
        if checkBreak:
            break
        else:
            continue
        canCheck = True
        currentPlayerCounter = 0
        for player in players:
            player.chips.roundBet = 0
        donePlayers = 0
        currentBet = 0
        
        if rnd == 'begin':
            print('\nFIRST ROUND\n')
            
            for player in players:
                player.chips.inRound = True

            startingBet = 5
            currentBet = 5
            currentPlayerCounter = 2
                            
        elif rnd == 'flop':
            print('\nFLOP\n')
            for card in range(3):
                communityCards.append(deck.deal())
            for player in players:
                if player.chips.inRound == True:
                    for card in communityCards:
                        player.add_card(card, True)
                    player.sort(player.fullHand)
                else:
                    donePlayers += 1
            printCommunityCards(communityCards)
            startingBet = 5
                            
        elif rnd == 'turn' or rnd == 'river':
            print("\n{}\n".format(rnd.upper()))
            
            for player in players:
                if player.chips.inRound == True:
                    player.add_card(deck.deal(), False)
                    player.sort(player.smallHand)
                    player.sort(player.fullHand)
                else:
                    donePlayers += 1
            
            printCommunityCards(communityCards)
            print(player)
            
            startingBet = 10
            
        checkBreak = bettingRound(players, currentPlayerCounter, numPlayers)
        
    winners = []
    winningType = "High Card"
    
    for player in players:
        player.winningHand, player.winningType = check_win(player.fullHand)
        if winningHands[player.winningType] < winningHands[winningType]:
            winningType = player.winningType
            winners.append(player)
        elif winningHands[player.winningType] == winningHands[winningType]:
            winners.append(player)
            
        winningCards = ""
        for card in player.winningHand:
            winningCards += card.rank +' of '+ card.suit
            if player.winningHand.index(card) != len(player.winningHand) - 1:
                winningCards += ", "
            else:
                winningCards += "."
        print("{} has a {}, with cards {}.".format(player.name, player.winningType, winningCards))
    
    if checkBreak:
        winner = checkBreak
        winners = [winner]
        print("{} has won {} chips by default with a {}.".format(winner.name, pot, winningType))
        winner.chips.win_pot()
        
    if len(winners) != 1:
        tieWinners = []
        while len(tieWinners) != 1:
            tieWinners = []
            emptyWinners = []
            high_card_val = "Two" 
            if len(winners) == 2:
                if count_cards(winners[0].fullHand) == count_cards(winners[1].fullHand):
                    tie = True
                else:
                    tie = False
            for winner in winners:
                # if winning hand == winning hand of other guy, then go onto the cards NOT in winning hand, as in full hand - winning hand
                if winner.winningHand == []:
                    emptyWinners.append(winner)
                    tieWinners.remove(winner)
                else:
                    winner_high_card = high_card(winner.winningHand)
                    if values[winner_high_card] < high_card_val:
                        high_card_val = winner_high_card
                        tieWinners = [winner]
                    elif values[winner_high_card] == high_card_val:
                        tieWinners.append(winner)
            if len(tieWinners) > 1:
                for winner in tieWinners:
                    for card in winner.winningHand:
                        if card.rank == high_card_val:
                            winner.winningHand.remove(card)
            elif tieWinners == []:
                tieWinners = emptyWinners
                for winner in tieWinners:
                    deleteHand = winner.winningHand
                    winner.winningHand = []
                    for card in winner.fullHand:
                        if card not in deleteHand:
                            winner.winningHand.append(card)
                    winner.winningHand, throwawayVar = check_win(winner.winningHand)
            winners = tieWinners
    
    if tie == True:
        #this doesnt work w three ppl w same hands, but honestly, that doesnt happen 
        print("{} and {} have won {} chips each with {}s.".format(winners[0].name, winners[1].name, pot//2, winningType))
        winners[0].chips.win_pot()
        winners[1].chips.win_pot()
    elif tie == False:
        winner = winners[0]                    
        print("{} has won {} chips with a {}.".format(winner.name, pot, winningType))
        winner.chips.win_pot()
                           
    play_again = input("Would you like to play another hand? >> ")
    if 'y' in play_again.lower():
        repick_players = input("Would you like to repick the players at the table? >> ")
        if 'y' in repick_players.lower():
            startingPlayer += 1
            sevencardstud(False, True)
        else:
            sevencardstud(False, False)
    else:
        print("Thank you for playing at Mika's Seven Card Stud Table!\nPlease play again and tell your friends!")
    