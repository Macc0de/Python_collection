# C:\python\Work1\direct
import os
import shutil


src = input('Введите путь до src: ')
if not os.path.exists(src):
    print('Такой папки не существует!')
    exit()
dst = input('Введите путь до dst: ')
if not os.path.exists(dst):
    print('Такой папки не существует!')
    exit()

flag = 0
for root, dirs, files in os.walk(src):
    for file in files:
        extension = file.split(".")[-1]
        if extension in ["png", "jpg", "jpeg"]:
            shutil.move(os.path.join(root, file), dst)
            flag = 1

if not flag:
    print("Картинок нет в папке src!")
    exit()

shutil.make_archive("new_archive", "zip", dst)
