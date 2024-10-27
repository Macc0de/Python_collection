import os


directory = input('Введите директорию: ')
if not os.path.exists(directory):
    print('Такой директории не существует!')
    exit()

extension = input('Введите расширение файла: ')

flag = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            print(file)  # print(os.path.abspath(file))
            flag = 1

if not flag:
    print('Нет файлов с таким расширением!')
