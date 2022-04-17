#replaces the domain of an email adress with a new domain. Removes spaces and copies to clipboard.
import pyperclip
badaddress = input('Enter an Email Adress. e.g John.Smith@gmail.com')
betteraddress = input('Enter a new email Domain (the part that comes after the @ symbol).')
CleanString = badaddress.strip()
CleanBetter = betteraddress.strip()
print('The original adress is',CleanString)
LocateAt = int(CleanString.find('@'))
if LocateAt == -1 :
    print('Email Addresses need an @ symbol. Try Again.')
else:
    snip = CleanString[LocateAt+1:]#Snips out the domain part of the adress.
    changes = badaddress.replace(snip,CleanBetter)
    #removing spaces
    SpaceReplacement = ''
    RemoveSpace = changes.replace(' ',SpaceReplacement)
    print('The new address is',RemoveSpace,'(any spaces have been removed and the address has been copied to your clipboard.)')
    pyperclip.copy(RemoveSpace)
