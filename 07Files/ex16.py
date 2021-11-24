def readFile():
    with open("lorem.txt") as file:
        counter = 0
        for line in file:
            print(line)
            counter += 1
            if counter % 5 == 0:
                enter = input("Press enter to read")
                
readFile()