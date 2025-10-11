import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
q = 7.25 * math.sin(x) - abs(y)
print("q =", q)
if x == 0:
    print("z: нельзя делить на ноль")
else:
    znam = y + 1 / math.sqrt(x * x + 10)
    if znam <= 0:
        print("z: корень из отрицательного числа")
    else:
        chisl = x + (2 + y) / (x * x)
        znam = math.sqrt(znam)
        z = chisl / znam
        print("z =", z)
