def arrayAppears(firstArray, secondArray):
    for firstElement in firstArray:
        if firstElement not in secondArray:
            return False
    return True

firstArray = [4, 5, 1, 2]
secondArray = [4, 1, 5, 2, 6, 2, 1]
print(arrayAppears(firstArray, secondArray))