# The user thinks of a secret no in mind (do not take input from user for sec no) 
# and the computer guesses the number.
#The change here is that everytime the computer guesses(will ask you high, low or correct), 
# you have to provide a feedback that 
# number is high, number is low and accordingly, guess again.

import random
def fun():
    upper= int(input("Enter the higher range"))
    lower=0
    guess_no='' #NO NEED TO initialise it again and again by keeping in while loop
    
    while(lower!=upper):
        number= random.randint(lower, upper)
        guess_no= input(f"Is {number} too high(H), too low(L) or correct?")
        if guess_no=='H':
            number=number-1
        elif guess_no=='L':
            number=number+1
        elif guess_no=='C':
            break
    print(f"The computer predicted the right number which is {number}")


fun()