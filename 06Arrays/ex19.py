def uniqueElements(array):
    uniqueArray = []
    for index in range(len(array)):
        found = False
        for uniqueIndex in range(len(array)):
            if index != uniqueIndex:
                if array[uniqueIndex] == array[index]:
                    found = True
        if found == False:
            uniqueArray.append(array[index])
    return uniqueArray

array = [2, 3, 2, 5, 8, 1, 9, 8]
print(f"Array: {array}")
print(f"Unique elements: {uniqueElements(array)}")