fileName = input("Enter file name: ")
file = open(fileName, "r")
count = 0
for line in file:
    count += 1

print(f"Number of lines: {count}")