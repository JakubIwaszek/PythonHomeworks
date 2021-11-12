import random

def getRandomElement(array):
    lenght = len(array)
    randomIndex = random.randint(0, lenght - 1)
    return array[randomIndex]

array = [3, 2, 6, 9, 0, 1, 13, 7, 24, 8]
print(getRandomElement(array))
print(getRandomElement(array))
print(getRandomElement(array))