import random

diceRoll = random.randint(1, 6)
rollGuess = int(input("Guess the rolled dice value: "))

if diceRoll == rollGuess:
    print("true")
else :
    print("false")