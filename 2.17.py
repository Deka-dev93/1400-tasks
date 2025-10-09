from math import sqrt
a = float(input("Большее основание: "))
b = float(input("Меньшее основание: "))
h = float(input("Высота: "))
c = sqrt(((a - b) / 2)**2 + h**2)
P = a + b + 2 * c
print("Периметр :", P)