flag = True
numbers = []
total = 0
while(flag == True):
    enteredNumber = int(input("Enter number: "))
    if enteredNumber == 0:
        flag = False
    else:
        numbers.append(enteredNumber)
        total += enteredNumber
mean = int(total / len(numbers))
print("RESULT: Quantity={0}, Sum={1}, Mean={2}".format(len(numbers), total, mean))