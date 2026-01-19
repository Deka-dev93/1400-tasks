a = float(input("Введите длину: "))
b = float(input("Введите ширину: "))
c = float(input("Введите высоту: "))
volume = a * b * c
side_area = 2 * (a * b + b * c + a * c)
print(f"Объем: {volume}")
print(f"Площадь поверхности: {side_area}")