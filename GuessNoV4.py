# The user thinks of a secret no in mind (do not take input from user for sec no) 
# and the computer guesses the number.
#The change here is that everytime the computer guesses(will ask you high, low or correct), 
# you have to provide a feedback that 
# number is high, number is low and accordingly, guess again.

import random
def fun():
    upper= int(input("Enter the higher range \n "))
    lower=0
    guess_no='' #NO NEED TO initialise it again and again by keeping in while loop
    A=[]
    while guess_no != 'C': #THINK HOW THIS while loop is going to end? It ends when we have C in respone
        number= random.randint(lower, upper)
        if number in A:
            continue
        guess_no= input(f"Is {number} too high(H), too low(L) or correct?")
        A.append(number)
        if guess_no=='H':
            number=number-1
        elif guess_no=='L':
            number=number+1
        

        
    print(f"The computer predicted the right number which is {number}")


fun()