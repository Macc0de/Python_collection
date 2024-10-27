with open("file.txt", 'r', encoding="utf-8") as file:
    data = file.read()

if not data:
    print("Файл пустой!")
    exit()

participants = list()
for i in data.split("\n"):  # Считывает полную строку - элемент списка
    if not i:  # От пустой строки
        continue

    name = i.split()
    if len(name) != 2:
        print("В строке должно содержаться 2 слова!")
        exit()

    grade = name[1]
    name = name[0]

    if not name.isalpha():
        print("В файле имя должно состоять только из букв!")
        exit()
    elif not grade.isdigit():
        print("В файле оценка должна состоять только из цифр!")
        exit()

    participants.append((name, int(grade)))  # Список: [(M, 12)]

participants.sort(key=lambda x: x[0])
for name, grade in participants:  # Вывод на консоль, сортировка по именам
    print(f"{name} {grade}", end='\n')
print()

participants.sort(key=lambda x: x[1], reverse=True)
for name, grade in participants:  # Вывод на консоль, сортировка по именам
    print(f"{name} {grade}", end='\n')

N = input("\nВведите значение N: ")
if not N.isdigit():
    print("Вы не ввели число!")
    exit()

good_students = list(filter(lambda student: student[1] > int(N), participants))
if not good_students:
    print("Нет таких участников, чья оценка превышает число N!")
    exit()

with open("res.txt", 'w', encoding="utf-8") as result:
    for name, grade in participants:
        if grade > int(N):
            result.write(f"{name} {grade}\n")
