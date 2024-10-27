import csv


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


with open("countries.csv", 'r', encoding="utf-8") as file:
    data = csv.reader(file, delimiter=',')
    if not data:
        print("Файл пустой!")
        exit()

    count = 0
    csv_data = list()
    for row in data:
        if count != 0:
            csv_data.append(row)
        else:
            count += 1

income_start = input("Введите начальную границу: ")
if not is_float(income_start):
    print("Неверный тип данных!")
    exit()

income_end = input("Введите конечную границу: ")
if not is_float(income_end):
    print("Неверный тип данных!")
    exit()

income_start = float(income_start)
income_end = float(income_end)
if income_start > income_end:
    print("Начальная граница больше конечной!")
    exit()

with open('income.csv', mode='w') as file:
    income = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in filter(lambda x: income_start <= float(x[2]) <= income_end, csv_data):
        income.writerow(row)

with open('inflation.csv', mode='w') as file:
    inflation = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in sorted(csv_data, key=lambda x: float(x[3])):
        inflation.writerow(row)

