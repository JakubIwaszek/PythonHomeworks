def separateNumbers(array):
    separatedArray = []
    for element in array:
        if element % 2 == 0:
            separatedArray.insert(0, element)
        else:
            separatedArray.append(element)
    return separatedArray
            
array = [4, 2, 7, 4, 3, 9, 0, 3, 5]
print(f"Array: {array}")
separatedArray = separateNumbers(array)
print(f"Separated array: {separatedArray}")