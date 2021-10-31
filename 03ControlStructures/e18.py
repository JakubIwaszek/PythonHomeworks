amount = int(input("Enter the amount in PLN: "))
total = 0
numberOf5 = 0
numberOf2 = 0
numberOf1 = 0

while total < amount:
    if total + 5 <= amount:
        total += 5
        numberOf5 += 1
    elif total + 2 <= amount:
        total += 2
        numberOf2 += 1
    elif total + 1 <= amount:
        total += 1
        numberOf1 += 1
else:
    print("The amount of PLN {0} in coins: ".format(amount))
    print("5zł - ", numberOf5)
    print("2zł - ", numberOf2)
    print("1zł - ", numberOf1)
