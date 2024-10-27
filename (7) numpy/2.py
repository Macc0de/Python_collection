import numpy as np
import numpy.random as rand


N = input("Введите размерность матрицы: ")
if not N.isdigit():
    print('Вы ввели не целое число!')
    exit()
N = int(N)
if N < 1:
    print('Размерность не может быть < 1!')
    exit()

A = np.matrix([rand.randint(1, 10, N) for i in range(N)])

print(A)

summa = A.sum(axis=0)
summa = summa.A1
minimum = summa.min()

print(f"Индекс столбца с минимальной суммой: {np.where(summa == minimum)[0][0]}")
