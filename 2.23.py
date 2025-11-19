import math
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
ploshad = a * b
perimetr = 2 * (a + b)
diagonal = math.sqrt(a**2 + b**2)
print("Результаты:")
print("Площадь прямоугольника:", ploshad)
print("Периметр прямоугольника:", perimetr)
print("Длина диагонали:", diagonal)