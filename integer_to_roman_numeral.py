# https://www.youtube.com/watch?v=ohBNdSJyLh8

# convert any whole number (0-9999) to roman numeral

user_input = input('please enter a whole number 0-999: ')

def build_roman(num):
   if(num == 0): return
   elif(num >= 1000): return 'M' + build_roman(num-1000)
   elif(num >= 900): return 'C' + build_roman(num+100)
   elif(num >= 500): return 'D' + build_roman(num-500)
   elif(num >= 400): return 'C' + build_roman(num+100)
   elif(num >= 100): return 'C' + build_roman(num-100)
   elif(num >= 90): return 'X' + build_roman(num+10)
   elif(num >= 50): return 'L' + build_roman(num-50)
   elif(num >= 40): return 'X' + build_roman(num+10)
   elif(num >= 10): return 'X' + build_roman(num-10)
   elif(num >= 9): return 'I' + build_roman(num+1)
   elif(num >= 5): return 'V' + build_roman(num-5)
   elif(num >= 4): return 'I' + build_roman(num+1)
   elif(num >= 1): return 'I' + build_roman(num-1)

if(user_input > 9999): print('you entered a number that is too large')
if(user_input < 0000): print('you entered a number that is too small')

print(build_roman(int(user_input)))