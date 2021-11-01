humanYears = int(input("Enter the dog's age in human years: "))
dogYears = 0

if humanYears < 0:
    print("Please insert right age.")
    exit()
elif humanYears <= 2:
    dogYears = humanYears * 10.5
else:
    dogYears = (10.5 * 2) + (humanYears - 2) * 4
    
print("The dog's age in dog’s years is {0} years.".format(int(dogYears)))