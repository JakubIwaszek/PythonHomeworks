def median(array):
    array.sort()
    lenght = len(array)
    if lenght % 2 == 0:
        center = int(lenght / 2)
        median = (array[center - 1] + array[center]) / 2
        return median
    else:
        center = int(lenght / 2)
        median = array[center]
        return median
    
firstArray = [1, 0, 9, 4, 6]
print(f"A: {firstArray}")
print(f"Median: {median(firstArray)}")
secondArray = [6, 8, 3, 1, 0, 5, 7]
print(f"B: {secondArray}")
print(f"Median: {median(secondArray)}")
