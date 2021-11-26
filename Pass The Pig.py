import random

def roll_pig():
    '''roll_pig() -> str
    rolls a pig, returns its side'''
    rollnum = random.random()  # rand number between 0 and 1
    if rollnum < 0.35:  # 35%
        return 'left'
    elif rollnum < 0.65: # next 30%
        return 'right'
    elif rollnum < 0.87: # next 22%
        return 'back'
    elif rollnum < 0.96: # next 9%
        return 'feet'
    elif rollnum < 0.99: # next 3%
        return 'nose'
    else: # last 1%
        return 'ear'

def roll_two_pigs():
    '''roll_two_pigs() -> (str,str,int)
    rolls two pigs
    returns the two rolls and the score'''
    # roll two pigs
    pig1 = roll_pig()
    pig2 = roll_pig()
    # compute score
    scores = {'left':0,'right':0,'back':5,'feet':5,'nose':10,'ear':15}
    score = scores[pig1]+scores[pig2]
    if pig1==pig2:
        score *= 2  # double score for pigs landing the same way
        # check for siders
        if score == 0:
            score = 1
    return (pig1,pig2,score)

def set_up_game():
    '''set_up_game() -> (list,list)
    returns a list of players' names and a list
    of whether the player is a computer'''
    numPlayers = ''
    while not numPlayers.isdigit():
        numPlayers = input("How many players: ")
    numPlayers = int(numPlayers)

    playerList = []  # initialize list of players
    computerList = []  # initialize computer player list
    computerCount = 0
    # get player data
    for n in range(numPlayers):
        computerPlayer = ''
        while not (computerPlayer=='y' or computerPlayer=='n'):
            computerPlayer = input("Player "+str(n+1)+": Is this player a computer (y/n): ")
        isComputer = (computerPlayer == 'y')
        computerList.append(isComputer)
        if isComputer:
            computerCount += 1
            playerList.append('(Computer' + str(computerCount) + ')')
        else:
            name = input("Enter your name: ")
            playerList.append(name)
    return playerList,computerList

def computer_choice(scoreList,turnScore,currentPlayer):
    '''computer_choice(scoreList,turnScore,currentPlayer) -> str
    makes the decision whether the computer rolls or stops
    returns 'roll' or 'stop'
    '''
    # definitely stop if computer has won
    if scoreList[currentPlayer]+turnScore >= 100:
        return 'stop'

    # continue if less than 10 scored this turn
    if turnScore < 10:
        return 'roll'

    # otherwise stop with probability (40 + turnScore)%
    if random.random() < 0.4 + turnScore/100:
        return 'stop'
    else:
        return 'roll'

def play_ptp():
    '''play_ptp() -> None
    plays a game of Pass the Pigs'''
    playerList,computerList = set_up_game()   # get players' names and types
    numPlayers = len(playerList) # number of players
    scoreList = [0]*numPlayers   # initialize scores
    currentPlayer = random.randrange(numPlayers) # choose who goes first

    winner = False
    while not winner: # play turns until someone wins
        input('\n'+playerList[currentPlayer]+", it's your turn!")
        turnScore = 0

        while True: # roll until Pig Out or player banks
            if computerList[currentPlayer]:  # computer player
                input("Press Enter for the computer to roll.")
            else:  # human player
                input("Press Enter to roll.")

            pig1,pig2,score = roll_two_pigs()
            if computerList[currentPlayer]:  # computer player
                input("Computer rolled "+pig1+" and "+pig2+".")
            else:  # human player
                input("You rolled "+pig1+" and " +pig2+".")

            if score == 0:  # bad roll - pig out
                input("Too bad -- PIG OUT!")
                turnScore = 0  # lose all points for the turn
                break          # turn ends

            input("This scores "+str(score)+".")
            turnScore += score # update score for this turn
            if computerList[currentPlayer]:  # computer player
                input("Computer scored "+str(turnScore)+" so far this turn.")
            else:  # human player
                input("You've scored "+str(turnScore)+" so far this turn.")

            choice = ''
            # get player's choice to roll again or stop
            if computerList[currentPlayer]:  # computer player
                choice = computer_choice(scoreList,turnScore,currentPlayer)
                if choice == 'roll':
                    input("Computer will roll again.")
                else:
                    input("Computer will stop.")
            else:  # human player
                while choice != 'roll' and choice != 'stop':
                    choice = input("Do you want to roll or stop? ")

            if choice=='stop':
                break  # end the turn

        # Turn is over, update the score
        scoreList[currentPlayer] += turnScore

        # Print the scores
        print()  # blank line
        for n in range(len(playerList)):  # print each player's score
            input(playerList[n]+" has "+str(scoreList[n])+" points")

        # Check for a winner
        if scoreList[currentPlayer] >= 100:  # we've got a winner!
            input(playerList[currentPlayer]+" wins!")
            winner = True  # end the game

        # Go on to the next player
        currentPlayer = (currentPlayer+1) % numPlayers
play_ptp()