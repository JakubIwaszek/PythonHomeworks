def findSecondLargest(array):
    largestNumber = array[0]
    secondLargestNumber = 0
    for element in array:
        if element > largestNumber:
            secondLargestNumber = largestNumber
            largestNumber = element
    for element in array:
        if element > secondLargestNumber and element < largestNumber:
            secondLargestNumber = element
    return secondLargestNumber

array = [5, 1, 9, 6, 1]
print(f"Array: {array}")
print(f"Result: {findSecondLargest(array)}")