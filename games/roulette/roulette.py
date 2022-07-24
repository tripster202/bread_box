import random

red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] # list
blk = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35] # list
grn = [37,38] # list

## ------ ------ ------ ##

def first_row(num):
   return num < 37 and num % 3 == 1

def second_row(num):
   return num < 37 and num % 3 == 2

def third_row(num):
   return num < 37 and num % 3 == 0

## ------ ------ ------ ##

def first_dozen(num):
   return num < 37 and int(num/12) < 1

def second_dozen(num):
   return num < 37 and int(num/12) == 1

def third_dozen(num):
   return num < 37 and int(num/12) > 1

## ------ ------ ------ ##

def try_luck(purse,unit_bet,happy):
   table_money = purse
   wager = unit_bet*2
   spins = 0; wins = 0; losses = 0; high = purse
   # ------ #
   while(table_money - wager > 0):
      table_money -= wager
      roll = random.randint(1,38); spins += 1
      if(second_dozen(roll) or third_dozen(roll)): wins += 1; table_money += unit_bet*3
      else: losses += 1
      if(table_money > high): high = table_money
      if(table_money >= happy): break
   # ------ #
   print('Money: $'+str(table_money))
   print('High: $'+str(high))
   print('Spins: '+str(spins))
   print('Wins:'+str(wins))
   print('Losses: '+str(losses))
   # ------ #

## ------ ------ ------ ##

if __name__ == "__main__":
   purse = int(input('Starting Amount: $'))
   unit_bet = int(input('Unit Bet: $'))
   happy = int(input('Happy Amount: $'))
   try_luck(purse,unit_bet,happy)