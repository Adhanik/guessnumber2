# The user comes up with a secret no and the computer guesses the number

import random
def guess(sec):
    x= int(input("Computer - Enter the outer range in which I have to guess\n"))
    num=0
    countif=0
    countelse=0
    #tot=0 No need to define extra variable for total. We can directly use sum of both.
    while(sec!=num):
        num= random.randint(1,x)
        if (num>sec):
            print(f"{num} is Too high. Guess again")
            countif+=1
        elif (num<sec):
            print(f"{num}Too Low. Guess again")
            countelse+=1
    tot=countif+countelse
    print(f"Yay!! computer you got the secret number {num} right in {tot} iteration!")


sec= int(input("Enter the secret number which comp will guess\n"))
guess(sec)