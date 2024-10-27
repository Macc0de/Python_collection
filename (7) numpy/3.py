import numpy as np
import os


def check_size(num):
    if not num.isdigit():
        print(f"Значение размерности должно быть целым числом! - '{num}'")
        return False
    elif int(num) < 1:
        print(f"Размерность не может быть < 1! - {num}")
        return False
    return True


def check_element(num):
    try:
        x = float(num)
    except ValueError:
        print(f"Элемент матрицы должен быть числом! - '{num}'")
        return False
    return True


path = input("Введите путь до файла: ")  # "info"
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

with open(path, 'r') as file:
    data = file.readline().split()
    if not data:
        print("Файл пустой!")
        exit()

    if len(data) < 2:
        print("Отсутствует значение размерности для A!")
        exit()

    n = data[0]  # Размерность A(nxm)
    m = data[1]
    if not check_size(n) or not check_size(m):
        exit()
    n = int(n)
    m = int(m)

    A = np.zeros((n, m), dtype=float)  # Создание A
    for i in range(n):
        line = file.readline().split()
        if len(line) < m:
            print("Отсутствует значение для матрицы A!")
            exit()
        for j in range(m):
            if not check_element(line[j]):
                exit()

            A[i, j] = float(line[j])

    print("A:")
    for i in range(n):
        for j in range(m):
            print(A[i, j], end=" ")
        print()

    data = file.readline().split()  # Размерность B(nx1)
    m = 1  # 1 столбец
    if len(data) < m:
        print("Отсутствует значение размерности для B!")
        exit()

    b_n = data[0]
    if not check_size(b_n):
        exit()
    b_n = int(b_n)

    if b_n != n:  # b_n = n(надо)
        print("Кол-во строк в м-це B должно быть равным кол-ву строк в м-це A!")
        exit()

    B = np.zeros((b_n, m), dtype=float)  # Создание B
    for i in range(m):
        line = file.readline().split()
        if len(line) < b_n:
            print("Отсутствует значение для матрицы B!")
            exit()
        for j in range(b_n):
            if not check_element(line[j]):
                exit()

            B[j, i] = float(line[j])

    print("\nB:")
    for i in range(b_n):
        for j in range(m):
            print(B[i, j], end=" ")
        print()

    # Нахождение вектора x
    A_trans = np.linalg.pinv(A)
    x = np.dot(A_trans, B)  # A_trans * B = x

    print("\nНайден x:")
    for i in range(len(x)):
        print(round(x[i,0], 2), end="\n")
