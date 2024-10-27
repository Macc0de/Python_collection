num = input("Введите число: ")

if not num.isdigit():
    print("Вы не ввели число!")
    exit()
elif int(num) < 1:
    print("Вы ввели число < 1!")
    exit()

maximum = num = int(num)
if num != 1:
    print(f"{num} -> ", end="")
else:
    print(num)

i = 1
while num != 1:
    if i % 5 == 0:
        print()
    i += 1

    if num % 2 == 0:
        num /= 2
    else:
        num *= 3
        num += 1

    if num > maximum:
        maximum = num

    if num != 1:
        print(int(num), end=" -> ")
    else:
        print(int(num))

print(f"\nСамое большое - {int(maximum)}\nКол-во элементов - {i}")
