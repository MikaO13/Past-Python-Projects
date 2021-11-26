import random
import turtle
wordfile = open('wordlist.txt','r')
words = wordfile.readlines()
wordfile.close()
wordlist = []
for each in words:
    wordlist.append(each)

def play_anagram():
    count = 0 #guesses
    print("Welcome to Mika's Anagram Game!\nUnscramble the letters to find the word!\n")
    orig = wordlist[random.randrange(len(wordlist))] #pick a random word
    orig = orig[:-1] 
    lst = list(orig) #turn word into a list
    while lst == list(orig):
        random.shuffle(lst) #shuffle word list
    scram = ""
    for char in lst: #put back into list
        scram += char
    #ask them to unscarmble it - give 3 guesses.
    print("You have three guesses.")
    print("Your word is: " + scram + '\n')
    while count < 3:
        guess = input("Guess: ")
        if guess == orig:
            print('\nYou have unscrambled the word!\nYOU WIN!')
            break
        count += 1
    if guess != orig:
        print('\nYou have not unscrambled the word.\nYOU LOSE')
    new_game = input("\nWould you like to play another hand? ")
    if 'yes' in new_game.lower():
        print('\n')
        play_anagram()
    else:
        print("Please come visit us at Mika's Anagram Game (or another of Mika's games) again soon!")

def play_hangman():
    wn = turtle.Screen()
    wn.clear()
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    wordstr = wordlist[random.randrange(len(wordlist))]
    word = list(wordstr)
    word.pop()
    player = []
    used = []
    hangman = []
    for item in word:
        player.append('_')
    print("\nWelcome to Hangman!\n\n")
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    dif = input("Would you like to play easy, medium, or hard? Auto is hard.\n")
    if 'easy' in dif.lower():
        lives = 10
        totallives = 10
    elif 'medium' in dif.lower():
        lives = 8
        totallives = 8
    else:
        if "e" or "m" in dif.lower():
            dif = input("Are you sure you want hard difficulty? If no, type 'easy' or 'medium'.")
            if dif.lower == "easy":
                lives = 10
                totallives = 10
            elif dif.lower == "medium":
                lives = 8
                totallives = 8
            else:
                lives = 6
                totallives = 6
        else:
            lives = 6
            totallives = 6
    while True:
        print('You have ' + str(lives) + ' lives remaining.')
        for letter in player:
            print(letter, end = " ")
        print('\n\nYou have used ', end = "")
        if used == []:
            print('no letters', end = " ")
        else:
            print('the letters', end = " ")
        for char in used:
            print(char, end = ' ')
        print('so far.')
        guess = input('What letter would you like to guess? ')
        while len(guess) != 1 or guess.isalpha() == False or guess in used:
            guess = input('What letter would you like to guess? ')
        guess = guess.lower()
        for letchr in range(0, len(word)):
            if guess == word[letchr]:
                player[letchr] = guess
        used.append(guess)
        used.sort()
        if guess not in word:
            lives -= 1
            print(guess + " is not in the word.")
        print("")
        if player == word:
            wn.clear()
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.right(180)
            t.forward(300)
            t.right(180)
            t.pendown()
            t.write("YOU WIN!", font=("Sans Serif", 100, "bold"))
            print("You guessed the word! You WIN!")
            break
        elif lives == totallives - 1 and "head" not in hangman:
            t.left(90)
            for i in range(360):
                t.forward(0.25)
                t.right(1)
            t.penup()
            t.right(90)
            t.forward(53)
            t.pendown()
            hangman.append("head")
        elif lives == totallives - 2 and "body" not in hangman:
            t.forward(25)
            t.right(180)
            t.forward(50)
            t.right(180)
            t.forward(25)
            t.right(180)
            t.left(60)
            hangman.append("body")
        elif lives == totallives - 3 and "leftarm" not in hangman:
            t.forward(30)
            t.right(180)
            t.forward(30)
            t.left(60)
            hangman.append("leftarm")
        elif lives == totallives - 4 and "rightarm" not in hangman:
            t.forward(30)
            t.right(180)
            t.forward(30)
            hangman.append("rightarm")
        elif lives == totallives - 5 and "leftleg" not in hangman:
            t.left(60)
            t.forward(25)
            t.right(30)
            t.forward(35)
            t.right(180)
            t.forward(35)
            t.right(120)
            hangman.append("leftleg")
        elif lives == totallives - 6 and "rightleg" not in hangman:
            t.forward(35)
            hangman.append("rightleg")
        elif lives == totallives - 7 and "lefteye" not in hangman:
            t.penup()
            t.back(90)
            t.left(100)
            t.forward(24)
            t.pendown()
            t.forward(6)
            t.back(3)
            t.right(90)
            t.forward(3)
            t.back(7)
            hangman.append("lefteye")
        elif lives == totallives - 8 and "righteye" not in hangman:
            t.penup()
            t.left(90)
            t.forward(11)
            t.right(90)
            t.forward(9)
            t.pendown()
            t.forward(7)
            t.back(3.5)
            t.right(90)
            t.forward(4.5)
            t.back(8)
            hangman.append("righteye")
        elif lives == totallives - 9 and "nose" not in hangman:
            t.penup()
            t.forward(13)
            t.pendown()
            t.forward(1)
            hangman.append("nose")
        elif lives == totallives - 10 and "mouth" not in hangman:
            t.penup()
            t.forward(6)
            t.pendown()
            t.left(120)
            for i in range(12):
                t.forward(1)
                t.left(1.5)
            hangman.append("mouth")
        if lives == 0:
            print("You ran out of lives. Game Over. :(")
            break
    print("The word was ", end = "")
    for letter in word:
        print(letter.upper(), end = "")
    playagain = input("\nPlay Again? ")
    if 'y' in playagain.lower():
        play_hangman()
    else:
        print("Thanks for playing, have a great day!")