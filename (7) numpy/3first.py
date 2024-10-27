import numpy as np
import os

'''
path = input("Введите путь до файла: ")  # "info"
if not os.path.exists(path):
    print('Файл не найден!')
    exit()'''

path = "info"
with open(path, 'r') as file:
    data = file.readline().split()
    if not data:  # Пуст ли файл
        print("Файл пустой!")
        exit()

    n = int(data[0])  # Размерность A(nxm)
    m = int(data[1])

    A = np.zeros((n, m), dtype=int)  # Создание A
    for i in range(n):
        line = file.readline().split()
        for j in range(m):
            A[i, j] = int(line[j])

    print("A:")
    for i in range(n):
        for j in range(m):
            print(A[i, j], end=" ")
        print()

    data = file.readline().split()  # Размерность B(nx1)
    n = int(data[0])
    m = 1

    B = np.zeros((n, m), dtype=int)  # Создание B
    for i in range(m):
        line = file.readline().split()
        for j in range(n):
            B[j, i] = int(line[j])

    print("B:")
    for i in range(n):
        for j in range(m):
            print(B[i, j], end=" ")
        print()
        
    # Нахождение вектора x
    A_trans = np.linalg.pinv(A)
    x = np.dot(A_trans, B)  # A_trans * B = x

    print("\nНайден x:")
    for i in range(len(x)):
        print(round(x[i,0], 2), end="\n")

