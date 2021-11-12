def displayArray(array):
    counter = 0
    for i in range(0, 8):
        print("-----", end="")
    print()
    for element in array:
        counter += 1
        print(f"|  {element}", end="")
        if counter % 8 == 0:
            print()
            for i in range(0, 8):
                print("-----", end="")
            print()
            counter = 0
        
    
array = range(1, 1000)
displayArray(array)