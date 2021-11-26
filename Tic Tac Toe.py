import random
def print_board(nums):
    '''
    Prints out the tic-tac-toe board
    '''
    print("  {} | {} | {}\n-------------\n  {} | {} | {} \n-------------\n  {} | {} | {}".format(nums[0],nums[1],nums[2],nums[3],nums[4],nums[5],nums[6],nums[7],nums[8]))
def turn(board, play, One, Two, AI):
    '''
    Run a player's turn in tic-tac-toe
    '''
    count = 0
    if play % 2 == 1:
        person = "Player One"
        piece = One
    else:
        person = "Player Two"
        piece = Two
    if AI == True and person == 'Player Two':
        move = random.randint(1,9)
        while board[move-1] == " ":
            move = random.randint(1,9)
    else:
        move = int(input("\n{}, where would you like to place your piece? ".format(person)))
        while True:
            if move not in range(1,10) or board[move-1] != " ":
                count += 1
                if count == 3:
                    return person + "'s turn has been skipped"
                else:
                    print("{}, you have {} more tries before your turn is skipped. ".format(person,3-count))
                    print("Please try to input a correct value. ")
                move = int(input("\n{}, where would you like to place your piece? ".format(person)))
            else:
                break
    board[int(move)-1] = piece
    print_board(board)
    return board
def check_win(pos, One):
    winner = "nobody"
    if pos[0] != " ":
        if pos[0] == pos[1] == pos[2]:
            if pos[0] == One:
                winner = "Player One"
            else:
                winner = "Player Two"
    return winner
        
def tictactoe():
    '''
    Play tic-tac-toe
    '''
    board = [" "," "," "," "," "," "," "," "," "]
    player = 1
    winner = ""
    win_sit = [[board[0],board[1],board[2]],[board[3],board[4],board[5]],[board[6],board[7],board[8]],[board[0],board[3],board[6]],[board[1],board[4],board[7]],[board[2],board[5],board[8]],[board[0],board[4],board[8]],[board[2],board[4],board[6]]]
    print("Welcome to Tic-Tac-Toe!\n")
    if 'no' not in input("Would you like to hear the rules? "):
        print("In this game, you place your pieces by typing the number corrosponding to the spot you would like to go. (ex: 2)")
        print_board([1,2,3,4,5,6,7,8,9])
        print("For example, with an empty board:")
        print_board(board)
        print("If you wanted to place an X in the top right spot, you would type 3.")
        print_board([" "," ","X"," "," "," "," "," "," "])
        print("If you try to place something in a spot that is already taken, you will be asked again\nwhere you would like to play. The same is true if you do not type something that is accepted.")
        print("\nNow that you know the rules, let's get started!\n")
    numPlayers = input('One Player or Two Player? ')
    OneChar = input("Player One, what would you like to use to represent your pieces?\nIf you leave this blank or input anything over one character (or a space), you will get the default, X.\nWhat piece do you want to represent you? ")
    if len(OneChar) != 1 or OneChar == " ":
        OneChar = "X"
    if numPlayers != 'Two Player':
        TwoChar = 'O'
        AI = True
    else:
        TwoChar = input("\nPlayer Two, what would you like to use to represent your pieces?\nIf you leave this blank, input anything over one character (or a space),\nor input the same as Player One, you will get the default, O.\nWhat piece do you want to represent you? ")
        if len(TwoChar) != 1 or TwoChar == " " or TwoChar == OneChar:
            TwoChar = "O"
        AI = False
    print("\n")
    print_board(board)
    while True:
        for pos in win_sit:
            if check_win(pos, OneChar) != "nobody":
                winner = check_win(pos,OneChar)
                print("\n\n{} WINS".format(winner))
                print("Congradulations, {}! You won in Tic-Tac-Toe!".format(winner))
                if 'yes' in input("Play Again? "):
                    tictactoe()
                else:
                    return "{} wins!".format(winner)
        if " " not in board:
            print("\n\nTIE")
            print("This game has resulted in a tie.")
            if 'yes' in input("Play Again? "):
                tictactoe()
            else:
                return "Tie Game"
        else:
            board = turn(board, player, OneChar, TwoChar, AI)
            player += 1
tictactoe()