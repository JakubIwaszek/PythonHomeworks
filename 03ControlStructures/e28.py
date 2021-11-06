firstNumber = 0
secondNumber = 1
sum = 0
count = 0
cache = 0

while(count < 50):
    if firstNumber == 0 and secondNumber == 1:
        print("{0} {1} ".format(firstNumber, secondNumber), end="")
    sum = firstNumber + secondNumber
    cache = secondNumber
    secondNumber = sum
    firstNumber = cache
    count += 1
    print("{0} ".format(sum), end="")
    