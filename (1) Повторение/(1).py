#  app,12,forge,from,apple,free,APP,append,34,311
#  upgrade,11,upp,UP,joga,noise,join,name,job,1
user_words = input("Введите 10 слов, разделенных запятой: ").rstrip(',').split(',')

if len(user_words) > 10:
    print("Вы ввели слишком много слов")  # Объект исключения
    exit()
elif len(user_words) < 10:
    print("Вы ввели меньше 10 слов")
    exit()

control = input("Введите контрольную строку: ")

if len(control) == 0:
    print("Вы не ввели контрольную строку")
    exit()

control_words = []
for word in user_words:
    if word.startswith(control):
        control_words.append(word)

if len(control_words) == 0:
    print("Таких слов нет")
else:
    print("Слова, которые начинаются с контрольной строки:", *control_words)
    #  print("Слова, которые начинаются с контрольной строки:", ", ".join(control_words))
