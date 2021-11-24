def openFile():
    file = open("lorem.txt", "r")
    for line in file:
        print(line)
    file.close()
        
openFile()