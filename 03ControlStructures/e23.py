for x in range(1, 10):
    for y in range(0, x):
        margin = x - 1
        if y == margin:
            print(x, end="\n")
        else:
            print(x, end="")