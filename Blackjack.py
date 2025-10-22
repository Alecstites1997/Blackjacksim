
#Importing libraries
import random, sys

#Setting up constants
Hearts = chr(9829)
Diamonds = chr(9830)
Clubs = chr(9824)
Spades = chr(9827)
Backside = 'Backside'

print(f'''Blackjack, by Al Sweigart al@inventwithpython.com
     Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
     The dealer stops hitting at 17.''')


def main ():
    money = 5000
    drawn_cards = drawfromdeck(num_cards=2)
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
               print(f''' Your current bet is {bet} and your remaining amount is {remainingmoney}''')
               print(f'''Your cards are: ''')
               for i in range(2):
                  for rank, suit in drawn_cards:
                     cardcreator(rank, suit)
                     print()
               print(f'''The dealer's cards are: ''')
               for i in range(2):
                  drawfromdeck()
      

            

         



            else:
              print('Thanks for playing!')
              break

def getbet(maxbet):
  print(f'''Your maximum bet is currently {maxbet}''')
  currentbet = input('What would you like your bet to be for this hand?')
  if int(currentbet) > int(maxbet):
     print('You are betting more money than you have, please try again')
     currentbet = input('What would you like your bet to be for this hand?')
  elif int(currentbet) <= int(maxbet):
     print('Great, lets play!')
  return currentbet

def drawfromdeck(num_cards=2):
   freshdeck = []
   drawndeck = []
   suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
   ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']

   for suit in suits:
      for rank in ranks:
        freshdeck.append(f'''{rank},{suit}''')
   i = 0
   while i <= 1:
      drawncards = (random.choice(freshdeck))
      i += 1
   drawncards = random.sample(freshdeck, num_cards)
   return(drawncards)

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





