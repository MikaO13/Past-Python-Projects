#Mastermind - started a while ago and never finished

colors = ['p', 'b', 'g', 'y', 'r', 'w'] # purple, blue, green, yellow, red, white

def determinePegs(guess, answer):
    white, red, pos = 0, 0, 0
    for pos in range(4):
        if guess[pos] == answer[pos]:
            red += 1
            answer[pos] = 'n' #n = none/done
            
    for answerPos in range(4):
        for guessPos in range(4):
            if guess[guessPos] == answer[answerPos]:
                white += 1
                answer[answerPos] = 'n'
    return (red, white)

def pickColors(name):
    failMessage = "Bad Input. Please remember to enter your choice in the format of cccc, \nwith each c being the first letter of a color in \npurple, blue, green, yellow, red, and white."
    while True:
        pick = input("{}, what would four colors are you picking? >> ".format(name))
        if len(pick) == 4:
            print(pick[0])
            if pick[0] in colors and pick[1] in colors and pick[2] in colors and pick[3] in colors:
                return pick
            else:
                print(failMessage)
        else:
            print(failMessage)

def mastermind(firstTime = True):
    hints = {}
    win = False
    
    if firstTime:
        print("Hello and Welcome to Mika's Mastermind Game!")
        print('Other games by Mika: Let It Ride, Seven Card Stud, Texas Hold Em, Blackjack, Pass the Pig, Hangman, Anagram, Go Fish, War, Uno, Connect 4\n')
        if 'y' in input('Would you like to hear the rules? ').lower():
            print('In this game, there are six colors - purple, blue, green, red, yellow, and white.\n'
                  'One player, the masterminder, will pick a code of four colors - there can be repeats - \n'
                  'and the other player, the guesser, will attempt to guess this code.\n'
                  "The guesser has 10 turns to guess the masterminder's code\n"
                  'In each turn the guesser will guess a code of four colors,\n'
                  'then will be told the number of red - correct colors in the correct place\n'
                  'and white - correct colors in the wrong place. With this information they will attempt to guess the code.\n'
                  'Good luck, and have fun!')
            
    masterminder = input("{}, what would you like to be called? >> ".format('Masterminder'))
    guesser = input("{}, what would you like to be called? >> ".format('Guesser'))
    
    if 'y' in input('Would you like to swap the masterminder and guesser? >> '):
        masterminder, guesser = guesser, masterminder
    
    code = pickColors('Masterminder ' + masterminder)
    print(code)
    
    for rnd in range(1, 11):
        print("It is round {}.".format(rnd))
        if len(hints) > 0:
            print("As a reminder, here are your hints thus far.")
            for colorHint in hints:
                print('{}: {} red and {} white.'.format(colorHint, hints[colorHint][0], hints[colorHint][1]))
    
        guess = pickColors('Guesser ' + guesser)
        hint = determinePegs(guess, [code[0], code[1], code[2], code[3]])
        hints[guess] = hint
        
        if hint == (4, 0):
            win = rnd
            break
    
    if win:
        print("Good job, {}! You have figured out {}'s code - {} - in {} rounds!".format(guesser, mastermind, code, win))
    else:
        print("Good job, {}! You have made a complicated enough code - {} - for {} to not figure it out!".format(mastermind, code, guesser))
    
    if 'y' in input("Would you like to play another hand? >> ").lower():
        repick_players = input("Would you like to repick the players at the table? >> ")
        mastermind(False)
    else:
        print("Thank you for playing at Mika's Mastermind Game Table!\nPlease play again and tell your friends!")

mastermind()