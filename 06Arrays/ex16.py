def star(n):
    stars = ""
    while(n > 0):
        stars += "*"
        n -= 1
    return stars

array = [12, 6, 4, 9, 10]
for element in array:
    print(f"{element}: {star(element)}")