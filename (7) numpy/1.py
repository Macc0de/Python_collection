import numpy as np
import numpy.random as rand


def create_matrix(size):
    return np.matrix([rand.randint(1, 101, size) for i in range(size)])


N = input("Введите размерность матриц: ")
if not N.isdigit():
    print('Вы ввели не целое число!')
    exit()
N = int(N)
if N < 1:
    print('Размерность не может быть < 1!')
    exit()
    
A = create_matrix(N)
B = create_matrix(N)

print(A)
print()
print(B)

print('\na > b?')
res = []
for i in range(N):
    sub_res = []
    for j in range(N):
        a = A[i, j]
        b = B[i, j]

        sub_res.append(a > b)

    res.append(sub_res)

C = np.matrix(res)
print(C)

print('a < b?')
res = []
for i in range(N):
    sub_res = []
    for j in range(N):
        a = A[i, j]
        b = B[i, j]

        sub_res.append(a < b)

    res.append(sub_res)

C = np.matrix(res)
print(C)

print('a == b?')
res = []
for i in range(N):
    sub_res = []
    for j in range(N):
        a = A[i, j]
        b = B[i, j]

        sub_res.append(a == b)

    res.append(sub_res)

C = np.matrix(res)
print(C)
