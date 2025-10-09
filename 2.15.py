from math import pi
R = float(input("Внешний радиус: "))
r = float(input("Внутренний радиус: "))
S = pi*(R**2 - r**2)
print("Площадь кольца: ", S)