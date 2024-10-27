from PIL import Image, ImageDraw, ImageFont
import os


def check(k, max):
    if not k.isdigit():
        print("Значение должно быть целым числом!")
        return False
    if 0 <= int(k) <= max:
        return True
    else:
        print("Неподходящее значение!")
        return False


def vertical_img(image):
    vertical_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    vertical_image.save("vertical_img.jpg")

    vertical_image.show()


def horizontal_img(image):
    horizontal_flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal_flip_image.save("horizontal_img.jpg")

    horizontal_flip_image.show()


def main_diagonal_img(image):
    main_diagonal_image = image.transpose(Image.TRANSPOSE)
    main_diagonal_image.save("main_diagonal_img.jpg")

    main_diagonal_image.show()


def side_diagonal_img(image):
    side_diagonal_image = image.transpose(Image.TRANSPOSE)
    side_diagonal_image = side_diagonal_image.transpose(Image.FLIP_LEFT_RIGHT)

    side_diagonal_image.save("side_diagonal_img.jpg")
    side_diagonal_image.show()


def sepia_img(image, k, width, height):
    sepia_image = image.copy()

    for y in range(height):  # По каждому пикселю
        for x in range(width):
            r, g, b = sepia_image.getpixel((x, y))  # Цвет с текущего пикселя

            red = min(int(0.393 * r + 0.769 * g + 0.189 * b), 255)  # Новые значения каналов
            green = min(int(0.349 * r + 0.686 * g + 0.168 * b), 255)
            blue = min(int(0.272 * r + 0.534 * g + 0.131 * b), 255)

            # Применяем коэффициент сепии к новым значениям цветовых каналов
            red = int(red * k + r * (1 - k))
            green = int(green * k + g * (1 - k))
            blue = int(blue * k + b * (1 - k))

            sepia_image.putpixel((x, y), (red, green, blue))  # Новый цвет пикселя

    sepia_image.save("sepia_img.jpg")
    sepia_image.show()


def plus_bright(image, k, width, height):
    plus_bright_image = image.copy()

    for y in range(height):
        for x in range(width):
            r, g, b = plus_bright_image.getpixel((x, y))

            new_r = min(int(r * k), 255)
            new_g = min(int(g * k), 255)
            new_b = min(int(b * k), 255)

            plus_bright_image.putpixel((x, y), (new_r, new_g, new_b))

    plus_bright_image.save("plus_bright_img.jpg")
    plus_bright_image.show()


def minus_bright(image, k, width, height):
    minus_bright_image = image.copy()

    for y in range(height):
        for x in range(width):
            r, g, b = minus_bright_image.getpixel((x, y))

            new_r = max(int(r * (1 - k)), 0)
            new_g = max(int(g * (1 - k)), 0)
            new_b = max(int(b * (1 - k)), 0)

            minus_bright_image.putpixel((x, y), (new_r, new_g, new_b))

    minus_bright_image.save("minus_bright_img.jpg")
    minus_bright_image.show()


def avg_color(image, width, height):
    sum_red = sum_green = sum_blue = 0

    for y in range(height):  # Суммирование компонент
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            sum_red += r
            sum_green += g
            sum_blue += b

    count_pixels = width * height
    avg_red = sum_red // count_pixels  # Средние значения
    avg_green = sum_green // count_pixels
    avg_blue = sum_blue // count_pixels

    new_image = Image.new("RGB", (1000, 1000), (avg_red, avg_green, avg_blue))
    new_image.show()


def add_text(image, text, coordinates):
    font_path = "CascadiaCode.ttf"  # arial.ttf
    font_size = 100
    text_color = (0, 255, 255)

    copy_image = image.copy()
    draw = ImageDraw.Draw(copy_image)

    font = ImageFont.truetype(font_path, font_size)  # Шрифт

    draw.text(coordinates, text, fill=text_color, font=font)  # Текст на изображении

    copy_image.save("text_image.jpg")
    copy_image.show()


def add_primitive(image, primitive, coordinates):
    copy_image = image.copy()

    color = (255, 20, 147)
    draw = ImageDraw.Draw(copy_image)

    if primitive == "ellipse":  # 30 200 300 325
        draw.ellipse(coordinates, fill=color)
    elif primitive == "line":  # 100 100 400 400
        draw.line(coordinates, fill=color, width=5)
    elif primitive == "arc":  # 200 100 400 300
        draw.arc(coordinates, start=0, end=360, fill=color, width=5)
    elif primitive == "rectangle":  # 200 150 300 500
        draw.rectangle(coordinates, fill=color)

    copy_image.save("primitive_image.jpg")
    copy_image.show()


path = input("Введите путь до изображения: ")  # "cat2.jpg"
if not os.path.exists(path):
    print('Изображение не найдено!')
    exit()

original_image = Image.open(path)
width, height = original_image.size

while 1:
    choose = input("Введите букву(a,b,c,d,e,f,g,h,i,j): ")
    if choose == 'a':
        vertical_img(original_image)
    elif choose == 'b':
        horizontal_img(original_image)
    elif choose == 'c':
        main_diagonal_img(original_image)
    elif choose == 'd':
        side_diagonal_img(original_image)
    elif choose == 'e':
        k = input("Введите коэффициент сепии(от 0 до 100 - проценты): ")
        if check(k, 100) is False:
            continue

        percent = int(k) / 100  # 90 - 0.90
        sepia_img(original_image, percent, width, height)
    elif choose == 'f':
        k = input("Введите коэффициент увеличения яркости(от 0 до 100 - проценты): ")
        if check(k, 100) is False:
            continue

        percent = 1 + int(k) / 100  # 90 - 1.90
        plus_bright(original_image, percent, width, height)
    elif choose == 'g':
        k = input("Введите коэффициент понижения яркости(от 0 до 100 - проценты): ")
        if check(k, 100) is False:
            continue

        percent = int(k) / 100  # 90 - 0.90
        minus_bright(original_image, percent, width, height)
    elif choose == 'h':
        avg_color(original_image, width, height)
    elif choose == 'i':
        text = input("Введите текст: ")
        if len(text) == 0:
            print("Пустая строка!")
            continue

        x = input(f"Введите координату x (0 <= x <= {width-1}): ")
        y = input(f"Введите координату y (0 <= y <= {height-1}): ")
        if check(x, width-1) is False or check(y, height-1) is False:  # Соответствие размерам
            continue

        coordinates = (int(x), int(y))
        add_text(original_image, text, coordinates)
    elif choose == 'j':
        primitive = input("Введите тип примитива(ellipse, line, arc, rectangle): ")
        if len(primitive) == 0:
            print("Пустая строка!")
            continue
        elif primitive != 'ellipse' and primitive != 'line' and primitive != 'arc' and primitive != 'rectangle':
            print("Неверный тип!")
            continue

        x1 = input(f"Введите координату x1 (0 <= x1 <= {width-1}): ")
        y1 = input(f"Введите координату y1 (0 <= y1 <= {height-1}): ")
        x2 = input(f"Введите координату x2 (0 <= x2 <= {width - 1}): ")
        y2 = input(f"Введите координату y2 (0 <= y2 <= {height - 1}): ")
        if check(x1, width-1) is False or check(y1, height-1) is False \
                or check(x2, width-1) is False or check(y2, height-1) is False:  # Соответствие размерам
            continue

        coordinates = (int(x1), int(y1), int(x2), int(y2))
        add_primitive(original_image, primitive, coordinates)
    else:
        print("Некорректный ввод!")
        break
