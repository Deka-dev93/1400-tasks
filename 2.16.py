from math import sqrt
a = float(input("Первый катет: "))
b = float(input("Второй катет: "))
c = sqrt(a**2 + b**2)
P = a + b + c
print("Периметр :", P)