firstNumber = 0
secondNumber = 1
total = 0
count = 0
cache = 0

while(count < 50):
    if firstNumber == 0 and secondNumber == 1:
        print("{0} {1} ".format(firstNumber, secondNumber), end="")
    total = firstNumber + secondNumber
    cache = secondNumber
    secondNumber = total
    firstNumber = cache
    count += 1
    print("{0} ".format(total), end="")
    