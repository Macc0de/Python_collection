import pandas as pd
import os


def check(num):
    if not num.isdigit():
        print("Значение должно быть целым числом!")
        return False
    elif int(num) < 0:
        print("Неподходящее значение!")
        return False
    return True


path = input("Введите путь до файла: ")
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

with open(path) as file:
    if os.fstat(file.fileno()).st_size:
        df = pd.read_csv(path, sep=";")
    else:
        print('Файл пуст!')
        exit()

# (1)
df = df.sort_values(by=["height_m"], ascending=False)
print("5 самых высоких зданий:")
print(df.head(5).to_string())

print("\n5 самых низких зданий:")
print(df.tail(5).to_string())

# (2)
print("\nМинимальная высота здания:")
print(df["height_m"].min())

print("\nМаксимальная высота здания:")
print(df["height_m"].max())

print("\nСредняя высота здания:")
print(round(df["height_m"].mean(), 2))

print("\nМедианная высота здания:")
print(df["height_m"].median())

# (3)
print("\nКол-во стран, упомянутых в файле:")
print(len(set(df["country"])))

# (4)
print("\nСамое старое здание:")
df = df.sort_values(by=["year_built"], ascending=True)
print(df.loc[df["year_built"] == df.head(1)["year_built"].values[0]][["name", "year_built"]].to_string(index=False))

print("\nСамое новое здание:")
print(df.loc[df["year_built"] == df.tail(1)["year_built"].values[0]][["name", "year_built"]].to_string(index=False))

# (5)
num = input("\nВведите кол-во этажей: ")
if not check(num):
    exit()

floor_limit = pd.DataFrame(df.loc[df["floors_above"] + df["floors_below_ground"] > int(num)])
if not len(floor_limit):
    print("Нет зданий с кол-вом этажей, большим чем ваше значение!")
else:
    print(floor_limit[["name", "floors_above", "floors_below_ground"]].to_string(index=False))

# (6)
year = input("\nВведите год: ")
if not check(year):
    exit()

choose_year = df.loc[df["year_built"] == int(year)]
if not len(choose_year):
    print("Нет зданий, построенных в этом году!")
else:
    print(choose_year[["name", "year_built"]].to_string(index=False))

# (7)
name_country = input("\nВведите страну: ")

choose_country = df.loc[df["country"] == name_country]
if not len(choose_country):
    print("Нет такой страны в файле!")
else:
    print("Кол-во зданий в этой стране:", len(choose_country))
    #print(choose_country["name"].to_string(index=False))
