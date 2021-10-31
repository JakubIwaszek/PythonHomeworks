height = int(input("Enter your height in cm: "))
weight = int(input("Enter your height in kg: "))
heightInM = height / 100
bmi = (weight) / (heightInM ** 2)
print("BMI Index: %.2f" % bmi)