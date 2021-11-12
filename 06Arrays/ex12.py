def reverseArray(array):
    reversedArray = []
    for element in array:
        reversedArray.insert(0, element)
    return reversedArray

array = [15, 8, 31, 47, 2, 19]
print(f"existedArray: {array}")
print(f"reversedArray: {reverseArray(array)}")