#A simple game of Cho-han, a traditional Japanese dice game.
#Players wager whether a pair of dice will come up even (Cho) or odd (Han).
#This program includes some basic input validation

import random
#import sys

total = 0
playAgain = True
wager = ''
result = ''

def getWager():
    global wager
    print('Welcome to cho-han. This is a tradtional Japanese dice game where players wager whether the total on a pair of dice will be even (Cho) or odd (Han).')
    print
    while wager == '':
      print('Chose your wager Cho (even) or Han (odd).')
      wager=input()
      if wager == 'Cho' or wager == 'Han':
        break
      else:
        print('Please enter a valid wager. Either Cho or Han.')
        wager = ''

def rollDice():
    global total, result
    total = random.randint(1,12)
    if total % 2 == 0:
      result = 'Cho'
    elif total %2 == 1:
      result = 'Han'

def giveResults():
    print('Total is ' + str(total))
    if wager == result:
        print('Congratulations! You win!')
    else:
        print('You lost. Better luck next time.')

def printVars():
    print('Total = ' + str(total))
    print('Result = ' + result)
    print('Wager = ' + wager)

def encore():
    global playAgain, wager
    encoreVar = ''
    while encoreVar == '':
      print('Would you like to play again? Y/N.')
      encoreVar = input()
      encoreVar = encoreVar.capitalize()
      if encoreVar == 'N':
        playAgain = False
        print('Thanks for playing!')
        #sys.exit
      elif encoreVar== 'Y':
        playAgain = True
        wager = ''
      else:
        print('Please enter Y or N')
        encoreVar = ''

while playAgain == True:
    getWager()
    rollDice()
    giveResults()
    printVars()
    encore()