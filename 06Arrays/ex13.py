def powerArray(array):
    poweredArray = []
    for element in array:
        poweredArray.append(element ** 2)
    return poweredArray

array = [8, 2, 5, 1, 9]
print(f"Array: {array}")
print(f"Scnd power: {powerArray(array)}")