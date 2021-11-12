def minmax(array):
    minmaxArray = []
    minmaxArray.append(min(array))
    minmaxArray.append(max(array))
    return minmaxArray

array = [4, 2, 8, 4, 7, 9, 5]
print(f"Array: {array}")
print(f"Result: {minmax(array)}")