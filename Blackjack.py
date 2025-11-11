
#Importing libraries
import random, sys

#Setting up constants
Hearts = chr(9829)
Diamonds = chr(9830)
Clubs = chr(9824)
Spades = chr(9827)
Backside = 'Backside'

def main ():
   #Define wallet and cards
    money = 5000
    deck = createfulldeck()
    playerdrawn_cards = drawfromdeck(deck, numcards = 2)
    dealerdrawn_cards = drawfromdeck(deck, numcards = 1)
    #Main loop for gameplay
    while True:
        if money <= 0:
            print(f'''You are broke, you should leave''')
            break
        #Loop path if you still have money
        elif money > 0:
            wanttoplay = input(f'''You still have money so do you want to play? ''')
            if wanttoplay == 'yes':
                #outline of the game
               print(f'''You current have {money}''')
               #What is my bet going to be?
               bet = int(getbet(money))
               remainingmoney = (money - bet)
               print(f'''Your current bet is {bet} and your remaining amount is {remainingmoney}''')
               print(f'''Your cards are: ''')
               #Draw 2 cards from the deck
               for rank, suit in playerdrawn_cards:
                  cardcreator(rank, suit)
                  print()
               print(f'''Your current total is {playerhandvalue(playerdrawn_cards)}''')
               
               print(f'''The dealer's cards are: ''')
               #Drawing first card from the deck for the dealer
               for rank, suit in dealerdrawn_cards:
                  cardcreator(rank, suit)
                  print()
               
               #Hit/stay logic
               if playerhandvalue(playerdrawn_cards) <= 21:
                  hit = input(f'''Do you want to hit again as dealer is showing {dealerhandvalue(dealerdrawn_cards)}? ''')
                  while hit == 'yes':
                     new_card = drawfromdeck(deck, numcards = 1)
                     playerdrawn_cards.append(new_card[0])
                     for rank, suit in new_card:
                        cardcreator(rank, suit)
                        print()
                        print(f'''After that hit, your current value is {playerhandvalue(playerdrawn_cards)}''')
                     hit = input(f'''Do you want to hit again as dealer is showing {dealerhandvalue(dealerdrawn_cards)}? ''')
                     dealernewcard = drawfromdeck(deck, numcards = 1)
                     dealerdrawn_cards.append(dealernewcard[0])
                     for rank, suit in dealerdrawn_cards:
                        cardcreator(rank, suit)
                     finaldealervalue = dealerhandvalue(dealerdrawn_cards)
                     print(finaldealervalue)
                     winlosslogic(playerdrawn_cards,dealerdrawn_cards)
                  while hit == 'no':
                     dealernewcard = drawfromdeck(deck, numcards = 1)
                     dealerdrawn_cards.append(dealernewcard[0])
                     for rank, suit in dealerdrawn_cards:
                        cardcreator(rank,suit)
                     finaldealervalue = dealerhandvalue(dealerdrawn_cards)
                     if finaldealervalue <= 17:
                        print(f'''Dealer has less than 17, so Dealer will draw another card''')
                        dealernewcard = drawfromdeck(deck, numcards = 1)
                        dealerdrawn_cards.append(dealernewcard[0])
                        for rank, suit in dealerdrawn_cards:
                           cardcreator(rank,suit)
                        finaldealervalue = dealerhandvalue(dealerdrawn_cards)

                     print(f'''The dealer is currently at {finaldealervalue}, while you are at {playerhandvalue(playerdrawn_cards)}''')
                     winlosslogic(playerdrawn_cards,dealerdrawn_cards)
                     break
                           
            else:
              print('Thanks for playing!')
              break
def winlosslogic(playerdrawn_cards, dealerdrawn_cards):
   if playerhandvalue(playerdrawn_cards) > 21:
      print(f'''You busted''')
   elif playerhandvalue(playerdrawn_cards) <= 21 and playerhandvalue(playerdrawn_cards) > dealerhandvalue(dealerdrawn_cards):
      print(f'''You won!''')

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
      card = deck.pop(random.randint(0, len(deck)-1))
      drawn.append(card)
   return drawn

def dealerhandvalue(cards):
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
   while aces > 0 and value > 21:
      value -= 10
      aces -= 1

   return value

def playerhandvalue(cards):
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
   while aces > 0 and value > 21:
         value -= 10
         aces -= 1
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





