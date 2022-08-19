#Slot machine

import random

#these are 3 seperate variables with random number between 1-10
a=random.randint(1,10)
b=random.randint(1,10)
c=random.randint(1,10)

#this is the variable used for the list of numbers used
spin=(a,b,c)

#This function prints the 3 numbers and is called later
def slots():    
 print(spin) 

#This is where the slots function is called  
slots()

#This function settles win conditions by checking if every value in the list is the same as the first 
def win(list):
 first = list[0]
 for val in list:
  if val != first:
   return False
   break
   return True
#This checks if the above statement is true or false if True it shows win if False returns lose 
if win(spin):
    print("Win!")
else:
    print("Lose!")
