def numberInRange(x, y):
    enteredNumber = int(input("Enter number: "))
    if enteredNumber > x and enteredNumber < y:
        return True
    else:
        return False
    
print(numberInRange(7, 51))