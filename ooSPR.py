#scissors paper rock remake, object oriented.
import random as r
computerOptions = ('Win', 'Loss', 'Draw')
playerOptions = ('s', 'p', 'r')

class ScissorsPaperRock:
#made on creation of the class.
    def __init__(self):
        self.name = input('enter your name: ')
        self.pScore = 0
        self.cScore = 0
        
    def makeChoice(self):
#gives the player a 'choice' although it doesn't matter what the player chooses. Generates a random value for the computer.
        incorrectChoice = True
        while incorrectChoice is True:
            self.pChoice = input(f'{self.name}, please choose S, P, or R: ').lower()
            if self.pChoice not in playerOptions:
                print(f'{self.name}, please enter a valid option.')
            else:
                incorrectChoice = False      
        self.cChoice = r.choice(computerOptions)

    def playGame(self):
#determines the outcome based on computers choice.
        if self.cChoice == 'Win':
            print(self.name,'You Win!')
            self.pScore = self.pScore + 1
        elif self.cChoice == 'Draw':
            print(self.name,'Its a draw!')
        else:
            print(self.name,'Computer Wins...')
            self.cScore = self.cScore + 1
        print(f'{self.name}, Your score is {self.pScore}. \nThe computers score is {self.cScore}')

#play the game
SPR = ScissorsPaperRock()
while True:
    SPR.makeChoice()
    SPR.playGame()
    validInput = True
#looping the game
    while validInput is True:
        check = input('Would you like to continue playing? Y or N').upper()
        if check == 'Y':
            validInput = False
            continue
        elif check == 'N':
            print(f'Thanks for playing')
            quit()
        else:
            print('Invalid response.')
            continue