import random
name = input('Welcome to Rock, Paper, Scissors. Please enter your name.')
playerscore = 0
computerscore = 0
playagain = True
#Repeated Functions
def playerwin():
    global playerscore
    print("You Win!")
    playerscore = playerscore + 1
def computerwin():
    global computerscore
    print("Computer Wins!")
    computerscore = computerscore + 1
def scoring():
    global playagain
    playerdisplay = print(name,"your score is",playerscore)
    computerdisplay = print("the computer's score is",computerscore)
    stop = input('Would you like to continue playing? Yes or No.').lower()
    if stop == 'yes':
        playagain = True
    else:
        playagain = False
#Looping Game
while playagain:
#Player Choice
    chosen = input('Please choose Scissors, Paper, or Rock.').lower()
    print("Your choice is",chosen)
#Computer Choice
    AIchoice = random.randint(1,3)
    if AIchoice == 1:
        print("Computer chose Scissors!")
    elif AIchoice == 2:
        print("Computer chose Paper!")
    else:
        print("Computer chose Rock!")
#Outcomes
    if chosen == "scissors" and AIchoice == 1:
        print("It's a Draw!")
    elif chosen == "scissors" and AIchoice == 2:
        playerwin()
    elif chosen == "scissors" and AIchoice == 3:
        computerwin()
    elif chosen == "paper" and AIchoice == 1:
        computerwin()
    elif chosen == "paper" and AIchoice == 2:
        print("It's a Draw!")
    elif chosen == "paper" and AIchoice == 3:
        playerwin()
    elif chosen == "rock" and AIchoice == 1:
        playerwin()
    elif chosen == "rock" and AIchoice == 2:
        computerwin()
    elif chosen == "rock" and AIchoice == 3:
        print("It's a Draw!")
    else :
        print('You have misspelt Scissors, Paper, or Rock.')
        continue

    scoring()

print('Thanks for playing',name)
