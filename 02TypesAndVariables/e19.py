a = int(input("Insert lenght of the a side: "))
b = int(input("Insert lenght of the b side: "))
c = int(input("Insert lenght of the c side: "))
p = (1/2) * (a + b + c)
area = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
print("Area of the triangle is: ", area)