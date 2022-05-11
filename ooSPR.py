#scissors paper rock remake, object oriented.
import random as r
computerOptions = ('Win', 'Loss', 'Draw')
againOptions = ('Y', 'N')

class ScissorsPaperRock:

    def __init__(self):
        self.name = input('enter your name: ')
        self.pScore = 0
        self.cScore = 0
        self.again = True
        
    def makeChoice(self):
        self.pChoice = input(f'{self.name}, please choose scissors, paper, or rock: ')
        self.cChoice = r.choice(computerOptions)

    def playGame(self):
        if self.cChoice == 'Win':
            print(self.name,'You Win!')
            self.pScore = self.pScore + 1
        elif self.cChoice == 'Draw':
            print(self.name,'Its a draw!')
        else:
            print(self.name,'Computer Wins...')
            self.cScore = self.cScore + 1
        print(f'{self.name}, Your score is {self.pScore}. \nThe computers score is {self.cScore}')

#Play the game
SPR = ScissorsPaperRock()
while True:
    SPR.makeChoice()
    SPR.playGame()
    check = input('would you like to continue playing? Y or N').upper()
    if check == 'Y':
        pass
    elif check == 'N':
        print('Thanks for playing.')
        quit()
    else:
        print('enter a valid response.')
        continue