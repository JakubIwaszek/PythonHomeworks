def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
number = int(input("Enter number: "))
array = [15, 38, 7, 23, 14]
if occurs(number, array) == True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} doesn't appear in the array")