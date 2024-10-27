from collections import defaultdict
from docxtpl import DocxTemplate
import csv


def get_year(data, year):  # Индекс года
    index = None
    for i, marathon in enumerate(data):  # (индекс, год)
        if marathon.get('year') == year:  # Значение по ключу
            index = i
            break  # Если найдено совпадение

    return index


def get_city(data, city):  # Индекс города
    index = None
    for i, marathon in enumerate(data):
        if marathon.get('title') == city:
            index = i
            break  # Если найдено совпадение, прерываем цикл

    return index


with open("data_marathon.csv", 'r', encoding="utf-8") as file:
    csv_data = list(csv.reader(file, delimiter=','))
    if not csv_data:
        print("Файл пустой!")
        exit()

#  Сортировка
data = list(sorted(csv_data, key=lambda x: x[0], reverse=True))  # Сортирует года

year_groups = defaultdict(list)  # Ключ(год): значение(список городов)

# Группирует данные по годам
for item in data:
    year = item[0]
    year_groups[year].append(item)

for year, year_data in sorted(year_groups.items(), reverse=True):  # Сортирует данные по городам внутри каждого года
    year_data.sort(key=lambda x: x[-1])

csv_data = list(year_groups.values())  # Делает данные обратно в формат csv файла
csv_data = [item for i in csv_data for item in i]  # Список списков -> сплошной список

# Создаем переменную для хранения всей информации
full_information = []
existed_year = {}

for i in csv_data:
    year = i[0]
    name = i[1]
    title = i[-1]
    type_human = i[2]
    result = i[-2]
    is_year_exist = get_year(full_information, year)  # Если такого нет года еще - None

    # Проверка есть ли год в full_information
    if is_year_exist is not None:
        is_city_exist = get_city(full_information[is_year_exist]["cities"], title)
    else:
        is_city_exist = None

    # Если нет года, то добавляем год и первый город
    if is_year_exist is None:
        data = {
            "year": year,
            "cities": [{
                "title": title,
                "humans": [{
                    "name": name,
                    "type": type_human,
                    "result": result
                }]
            }]
        }
        full_information.append(data)
    # (Добавляет в текущий год)Если нет текущего города, то добавляем его и информацию о людях из этого города
    elif is_city_exist is None:
        data = {
            "title": title,
            "humans": [{
                "name": name,
                "type": type_human,
                "result": result
            }]
        }
        full_information[is_year_exist]["cities"].append(data)
    else:  # Добавляет человека в город и год, которые уже созданы
        data = {
            "name": name,
            "type": type_human,
            "result": result
        }
        full_information[is_year_exist]["cities"][is_city_exist]["humans"].append(data)

# Загружаем шаблон документа
template = DocxTemplate("sample.docx")

#  Рендер шаблона
template.render({'marathon_info': full_information})

template.save("marathon.docx")
