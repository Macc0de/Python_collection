with open("file1.txt", 'r', encoding="utf-8") as file:
    data = file.read()

if not data:
    print("Файл пустой!")
    exit()

characters_occurrence = {}

for i in data:
    letter = i.lower()

    if letter.isalpha():
        characters_occurrence[letter] = characters_occurrence.get(letter, 0) + 1

if not characters_occurrence:
    print("В файле нет букв!")
    exit()

with open("res1.txt", 'w', encoding="utf-8") as result:
    for letter, count in characters_occurrence.items():
        result.write(f"{letter}: {count}\n")

