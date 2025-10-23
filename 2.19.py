from math import sqrt, sin
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
chisx = (2 / (a**2 + 25)) + b
znamx = sqrt(b + (a + b) / 2)
x = chisx/ znamx
chisy= abs(a) + 2 * sin(b)
znamy = 5.5 * a
y = chisy/ znamy
print("x = ", x )
print("y = ", y )
