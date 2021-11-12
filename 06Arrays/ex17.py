def doNotContains(firstArray, secondArray):
    for element in firstArray:
        if element not in secondArray:
            print(element)
            
firstArray = [4, 36, 12, 28, 9, 44, 5]
secondArray = [5, 1, 36]
doNotContains(firstArray, secondArray)