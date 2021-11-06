n = int(input("Enter number: "))
primeNumbers = []
x = 1
while(len(primeNumbers) < n):
    x += 1
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                break
            else:
                primeNumbers.append(x)
                break
print("Prime numbers: ", primeNumbers)