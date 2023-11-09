import random

#random jackpot number
jackpot = random.randint(1,100)
#guessing the number
guess = int(input("Make A Guess : "))
#count the number of attempts
count = 1

#conditions
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    #if failed to guess then guess again
    guess = int(input("Make A Guess : "))
    #increment count
    count+=1
print("You Guessed Successfully")
print("You took ",count," attempts")