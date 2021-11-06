elementInRowCount = 0
rows = 7
cacheNumber = 1
startingNumber = 1
for number in range(1,50):
    print(cacheNumber, end = " ")
    elementInRowCount += 1
    cacheNumber = cacheNumber + rows
    if elementInRowCount == rows:
        print()
        elementInRowCount = 0
        startingNumber += 1
        cacheNumber = startingNumber