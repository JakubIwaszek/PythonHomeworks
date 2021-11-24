import stack

def convertToBinary(number):
    while number > 0:
        division = number / 2
        number = int(division)
        remainder = int(division % 2)
        stack.push(remainder)
    
convertToBinary(18)
stack.display()