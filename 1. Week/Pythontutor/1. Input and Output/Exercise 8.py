#a - расстояние между рядами
#b - расстояние между дырками
#L - длина своболного конца шнурка
#N - количество дырок в ряду  
a = int(input()) # всегда две штуки
b = int(input()) #всегда 2 штуки
L = int(input()) #всегда умножаем на 2 
N = int(input()) 

a1 = (a * 2) * (N - 1) + a
b1 = (b * 2) * (N - 1)
L1 = (L * 2)

print ((a1 + b1 + L1))