def stringArray(array):
    text = ""
    for index in range(len(array)):
        if index == len(array) - 1:
            text += f"{array[index]}"
        else:
            text += f"{array[index]}, "
    return text

array = [5, 4, 3, 2, 6, 5]
print(f"Array: {array}")
string = stringArray(array)
print(f"String: {string}")