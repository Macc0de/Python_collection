import numpy as np
import os


path = input("Введите путь до файла: ")
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

with open(path) as file:
    if os.fstat(file.fileno()).st_size:
        data = np.loadtxt(path, delimiter=";", dtype=str, skiprows=1)
    else:
        print('Файл пуст!')
        exit()
#print(data)

# (1)
print("\nСредняя цена за курс:")
print(np.average(data[:, 1].astype(int)))  # Строка в число
# [row, column]

# (2)
print("\nМинимальное число подписчиков:")
print(np.min(data[:, 2].astype(int)))

# (3)
print("\nМаксимальная продолжительность лекций:")
print(np.max(data[:, -1].astype(float)))

# (4)
print("\nУровень с макс. кол-вом курсов:")

courses = np.unique(data[:, -2])  # Уникальные курсы
count = {}
for course in courses:
    rows, cols = np.where(data == course)
    count[len(data[rows])] = course

#print(count)
print(count[max(count)])  # Ключ с максимальным значением
