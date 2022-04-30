#If number is a multiple of 3, output is fizz.
#If number is a multiple of 5, output is buzz.
#If number is a multiple of both, output is fizzbuzz.
nrange = input('enter the number which will be counted to: ')
try :
    nrange = int(nrange)
except :
    print('please enter a numberical value.')
    quit()

for number in range(1, nrange + 1) :
    if number % 3 == 0 and number % 5 == 0:
        print(number,'fizz buzz.')
    elif number % 3 == 0 :
        print(number,'fizz.')
    elif number % 5 == 0 :
        print(number,'buzz.')
    else :
        print(number)
