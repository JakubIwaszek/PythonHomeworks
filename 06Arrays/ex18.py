def bubbleSort(array):
    numberOfElements = len(array)
    for i in range(numberOfElements - 1):
        for j in range(0, numberOfElements-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
                
firstArray = [3, 1, 5, 32, 7, 31, 65]
secondArray = [90, 54, 2, 32, 6, 78, 5, 1]
thirdArray = [1, 43, 2, 81, 42, 99, 6]

print(bubbleSort(firstArray))
print(bubbleSort(secondArray))
print(bubbleSort(thirdArray))