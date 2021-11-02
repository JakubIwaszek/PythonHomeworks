a = int(input("Enter a rectangle dimension: "))
b = int(input("Enter b rectangle dimension: "))

for x in range(0, a):
    for y in range(0, b):
        margin = b - 1
        if y == margin:
            print("*", end="\n")
        else:
            if y > 0 and x > 0 and x < (a-1):
                print(" ", end="")
            else:
                print("*", end="")