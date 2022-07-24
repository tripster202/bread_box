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

def try_luck(unit_bet,happy):
   spins = 0; wins = 0; losses = 0;
   roll = random.randint(1,38)

## ------ ------ ------ ##

if __name__ == "__main__":
   try_luck()