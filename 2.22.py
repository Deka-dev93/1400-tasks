import math
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
ma = abs(a)
mb = abs(b)
arifm = (ma + mb) / 2
geom = math.sqrt(ma * mb)
print("Результаты вычисления:")
print("Модуль первого числа:", ma)
print("Модуль второго числа:", mb)
print("Среднее арифмитическое модулей:", arifm)
print("Среднее геометрическое модулей", geom)