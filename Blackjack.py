
#Importing libraries
import random, sys

#Setting up constants
Hearts = chr(9829)
Diamonds = chr(9830)
Clubs = chr(9824)
Spades = chr(9827)
Backside = 'Backside'

def main ():
    money = 5000
    deck = createfulldeck()
    playerdrawn_cards = drawfromdeck(deck, numcards = 2)
    dealerdrawn_cards = drawfromdeck(deck, numcards = 1)
    while True:
        if money <= 0:
            print(f'''You are broke, you should leave''')
            break
        elif money > 0:
            wanttoplay = input(f'''You still have money so do you want to play? ''')
            if wanttoplay == 'yes':
                #outline of the game
               print(f'''You current have {money}''')
               bet = int(getbet(money))
               remainingmoney = (money - bet)
               print(f'''Your current bet is {bet} and your remaining amount is {remainingmoney}''')
               print(f'''Your cards are: ''')
               for rank, suit in playerdrawn_cards:
                  cardcreator(rank, suit)
                  print()
               print(f'''Your current total is {handvalue(playerdrawn_cards)}''')
               
               print(f'''The dealer's cards are: ''')
               for rank, suit in dealerdrawn_cards:
                  cardcreator(rank, suit)
                  print()
            
                  
      

            

         



            else:
              print('Thanks for playing!')
              break

def getbet(maxbet):
  print(f'''Your maximum bet is currently {maxbet} ''')
  currentbet = input('What would you like your bet to be for this hand? ')
  if int(currentbet) > int(maxbet):
     print('You are betting more money than you have, please try again ')
     currentbet = input('What would you like your bet to be for this hand? ')
  elif int(currentbet) <= int(maxbet):
     print('Great, lets play!')
  return currentbet

def createfulldeck():
   deck = []
   suits = [Hearts, Clubs, Spades, Diamonds]
   ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']

   for suit in suits:
      for rank in ranks:
        deck.append((rank,suit))
   return deck

def drawfromdeck(deck, numcards=2):
   drawn = []
   for _ in range(numcards):
      card = deck.pop()
      drawn.append(card)
   return drawn

def handvalue(cards):
   value = 0
   aces = 0
   for rank, suit in cards:
      if rank in ['J', 'Q', 'K']:
         value += 10
      elif rank == 'A':
         aces += 1
         value += 11
      else:
         value += int(rank)
   if aces != 0:
      acevalue = input(f'''You are currently at {value}, would you like to have ace count as 11 or 1?''')
      if acevalue == '1':
         value -= 10
   return value

def cardcreator(rank, suit):
   if len(str(rank)) == 1:
      x = rank 
      print(f'''
             ___
            |{x}  |
            | {suit} |
            |__{x}|''')
   elif len(str(rank)) == 2:
      x = rank
      print(f'''
             ___
            |{x} |
            | {suit} |
            |_{x}|''')


main()





