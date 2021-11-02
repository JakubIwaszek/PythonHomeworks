index = 1
flag = True
for x in range(1, 6):
    for y in range(0, x):
        margin = x - 1
        if y == margin:
            print("*", end="\n")
        else:
            print("*", end=" ")
            
for x in range(4, 0, -1):
    for y in range(0, x):
        margin = x - 1
        if y == margin:
            print("*", end="\n")
        else:
            print("*", end=" ")