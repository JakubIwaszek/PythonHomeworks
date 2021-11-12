def difference(array):
    minNumber = min(array)
    maxNumber = max(array)
    return maxNumber - minNumber
    
array = [5, 1, 9, 6, 1]
print(f"Array: {array}")
print(f"Result: {difference(array)}")