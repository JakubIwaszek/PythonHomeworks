def sumOfDigits(digits):
    sum = 0
    while digits:
        sum += digits % 10
        digits //= 10
    return sum

print(sumOfDigits(7182))