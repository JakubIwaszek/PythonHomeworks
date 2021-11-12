def fetchGreaterNumbers(number, array):
    greaterNumbers = []
    for element in array:
        if element > number:
            greaterNumbers.append(element)
    return greaterNumbers

number = int(input("Enter number: "))
array = [3, 6, 65, 4, 23, 87, 5, 7, 4, 1, 25, 14]
greaterNumbers = fetchGreaterNumbers(number, array)
print(f"Greater numbers: {greaterNumbers}")