def copyFile():
    with open("lorem.txt") as file:
        data = file.read()
        with open("loremCopy.txt", "w") as copy:
            copy.write(data)

copyFile()