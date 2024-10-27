# folder_with_file_and_photos.zip
import os
import shutil


archive = input('Введите архив: ')  # Ввести без .zip
if not os.path.exists(archive):
    print('Такого архива не существует!')
    exit()

new_folder = input("Введите название папки куда разархивировать архив:\n")
while 1:
    if os.path.exists(new_folder):  # Если такая папка уже есть
        new_folder = input("Такая папка уже существует! Введите другое название:\n")
        continue
    break

shutil.unpack_archive(archive, new_folder, "zip")

size = 0
for root, dirs, files in os.walk(new_folder):
    for file in files:
        size += os.path.getsize(os.path.join(root, file))

print(size, "bytes")
print(round(size/1000, 2), "kilobytes")
# shutil.rmtree(new_folder)  # Удалить созданную папку
