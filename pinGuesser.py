#guess a 4 digit numerical pin.
import random as r
guessed = False
attemptCount = 0

#make a random pin:
def pinMake():
    global guessedPin
    guessedPin = ''
    for i in range(4):
        i = str(r.randint(0,9))
        guessedPin = guessedPin + i
pinMake()

#Guess the pin:
def pinGuess():
    global fourDigit
    fourDigit = ''
    for l in range(4):
        l = str(r.randint(0,9))
        fourDigit = fourDigit + l
    print(fourDigit)

#repeat guesses until correct:
while guessed is False:
    pinGuess()
    attemptCount = attemptCount + 1
    if fourDigit == guessedPin:
        guessed = True
        print('Pin',guessedPin,'guessed in',attemptCount,'attempts')