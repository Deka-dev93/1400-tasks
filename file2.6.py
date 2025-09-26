from  math import sqrt
h = float(input("Высота = "))
R = 6350
d = sqrt(2 * R * h + h**2)
print("Расстояние до линии горизонта: ", d)