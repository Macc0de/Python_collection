import json


with open("animals.json", 'r', encoding="utf-8") as file:
    data = file.read()
    if not data:
        print("Файл пустой!")
        exit()

    data = json.loads(data).get("animals")

filtered_types = list(filter(lambda animal: animal.get("animal_type"), data))
if not filtered_types:
    print("Поле animal_type не найдено в файле!")
    exit()
else:
    search_birds = list(filter(lambda x: x.get("animal_type") == "Bird", filtered_types))
    if search_birds:
        print(json.dumps(search_birds, indent=2))
    else:
        print("Тип животного Bird не найден!")

    print("Кол-во дневных животных:", len(list(filter(lambda x: x.get("active_time") == "Diurnal", filtered_types))))

    print("\nЖивотное с наименьшим весом:")
    animals_weight = list(filter(lambda x: x.get("weight_min"), filter(lambda x: True, data)))
    if not animals_weight:
        print("Поле с минимальным весом не найдено!")
    else:
        print(json.dumps(min(animals_weight, key=lambda x: x["weight_min"]), indent=2))
