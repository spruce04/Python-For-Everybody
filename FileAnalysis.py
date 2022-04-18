#Give the wordcount of a file
Fname = input('enter a file name')
try :
    OpenFile = open(Fname)
except :
    print('That file could not be found.')
    quit()
Storage = list()
for line in OpenFile :
    linel = line.lower()
    lineA = linel.split()
    Storage = Storage + lineA

print('the total wordcount is',(len(Storage)))

#Count the amount of times a chosen word occurs.
RepeaterA = True
while RepeaterA :
    countword = input('Type the word which you would like to count.').lower()
    counting = Storage.count(countword)
    print('The word',countword,'occurs',counting,'times.')
    Continue = input('Would you like to repeat this process?').lower()
    if Continue != 'yes' :
        break 

#Give each individual word once in alphabetical order.
individual = dict.fromkeys(Storage)
individuallist = list(individual)
Ipresent = sorted(individuallist)
print('Each individual word in alphabetical order:',Ipresent)
print('There are',len(Ipresent),'different individual words.')

#Find the most commonly occuring word.
commonwordcount = 0
for word in Storage :
    counter = Storage.count(word)
    if commonwordcount < counter :
        commonwordcount = counter
        commonword = word
              
print('The word:',commonword,'. is the most commonly occuring word, occuring',commonwordcount,'times.' )
print('program finished')
