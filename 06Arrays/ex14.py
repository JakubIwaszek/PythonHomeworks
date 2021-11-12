def displayLongestName(array):
    longestName = array[0]
    for element in array:
        if len(element) > len(longestName):
            longestName = element
    return longestName

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print(f"Names: {array}")
print(f"Longest name: {displayLongestName(array)}")