import random

def writeRandomNumbers():
    with open("numbers", "w") as file:
        numbers = ""
        for x in range(1, 51):
            randomNumber = random.randint(100, 999)
            numbers += f"{randomNumber}\n"
        file.write(numbers)
            
writeRandomNumbers()