def openFile():
    with open("lorem.txt") as file:
        for line in file:
            print(line)
            
openFile()