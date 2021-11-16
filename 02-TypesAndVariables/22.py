import random

dice = random.randrange(1,6)
guess = ""
while(guess != dice):
    guess=int(input("Guess the number: "))
print(f"{guess} is correct answer!")