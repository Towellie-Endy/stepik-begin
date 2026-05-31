# ТЕМА 2. + экзамен 3

# cost1 = int(input())
# cost2 = int(input())
# cost3 = int(input())
# cost4 = int(input())

# print((cost1 + cost2 + cost3 + cost4) * 3)


# a = int(input())
# b = int(input())

# print(3 * ((a + b) * (a + b) * (a + b)) + 275 * b * b - 127 * a - 41)


# number = int(input())

# print(f'Следующее за числом {number} число: {number + 1}')
# print(f'Для числа {number} предыдущее число: {number - 1}')


# lenght = int(input())

# print(f'Объем = {lenght * lenght * lenght}')
# print(f'Площадь полной поверхности = {6 * (lenght * lenght)}')


# a = int(input())
# b = int(input())

# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')


# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# rez = (num_1 + num_2 * (num_3 - 1))

# print(rez)  


# num = int(input())

# print(num, num * 2, num * 3, num * 4, num * 5, sep='---')


# b1 = int(input())
# q = int(input())
# n = int(input())

# print(b1 * (q ** (n - 1)))


# students = int(input())
# mandarin = int(input())

# print(mandarin // students)
# print(mandarin % students)


# n = int(input())

# print(n % 2 + n // 2)


# how_minutes = int(input())

# print(f'{how_minutes} мин - это {how_minutes 2// 60} час {how_minutes % 60} минут.')


# place = int(input())

# print((place - 1)// 4 + 1)


# digit = int(input())
# first = digit // 100
# second = digit // 10 % 10
# third = digit % 10

# print(f'Сумма цифр = {first + second + third}')
# print(f'Произведение цифр = {first * second * third}')


# digit = int(input())
# first = digit // 100
# second = digit // 10 % 10
# third = digit % 10

# print(f'{first}{second}{third}')
# print(f'{first}{third}{second}')
# print(f'{second}{first}{third}')
# print(f'{second}{third}{first}')
# print(f'{third}{first}{second}')
# print(f'{third}{second}{first}')


# digit = int(input())
# first = digit // 1000
# second = digit // 100 % 10
# third = digit // 10 % 10
# fouth = digit % 10

# print(f'Цифра в позиции тысяч равна {first}')
# print(f'Цифра в позиции сотен равна {second}')
# print(f'Цифра в позиции десятков равна {third}')
# print(f'Цифра в позиции единиц равна {fouth}')


# print(17 * '*')
# print('*', 13 * ' ', '*')
# print('*', 13 * ' ', '*')
# print(17 * '*')


# num_1 = int(input())
# num_2 = int(input())

# print(f'Квадрат суммы {num_1} и {num_2} равен {(num_1 + num_2) ** 2}')
# print(f'Сумма квадратов {num_1} и {num_2} равна {num_1 ** 2 + num_2 ** 2}')


# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# num_4 = int(input())

# print(num_1 ** num_2 + num_3 ** num_4)


# a = int(input())
# b = str(a)

# print(a + int(b * 2) + int(b * 3))


# ТЕМА 4.

# str_1 = input()
# str_2 = input()

# print('Пароль принят' if str_1 == str_2 else 'Пароль не принят')


# a = int(input())

# print('Четное' if a % 2 == 0 else 'Нечетное')


# age = int(input())

# print('Доступ разрешен' if age >= 18 else 'Доступ запрещен')


# a = int(input())
# b = int(input())

# print(a if a < b else b)


# a = int(input())
# b = int(input())
# c = int(input())

# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')


# digit = int(input())
# first = digit // 1000
# second = digit // 100 % 10
# third = digit // 10 % 10
# fouth = digit % 10
# if first + fouth == second - third:
#     print('ДА')
# else:
#     print('НЕТ')

# a = int(input())
# b = int(input())
# c = int(input())
# count = 0
# if a > 0:
#     count += a
# if b > 0:
#     count += b
# if c > 0:
#     count += c
# print(count)

# age = int(input())
# if age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if age >= 60:
#     print('старость')


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(min(a, b, c, d))



# x = int(input())

# if -30 < x <= -2 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# beauty_number = int(input())
# numb = beauty_number // 1000
# if 1 <= numb < 10 and (beauty_number % 7 == 0 or beauty_number % 17 == 0):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# c = int(input())

# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')


# year = int(input())
# print('YES' if year % 4 == 0 and not(year % 100 == 0) or year % 400 == 0 else 'NO')


# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())

# if a1 == a3 or a2 == a4:
#     print('YES')
# else:
#     print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
#     print('YES')
# else:
#     print('NO')



# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or c == a:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# a = int(input())
# b = int(input())
# c = int(input())

# if a > b > c or c > b > a:
#     print(b)
# if a > c > b or b > c > a:
#     print(c)
# if b > a > c or c > a > b:
#     print(a)


# 1 3 5 7 8 10 12   31
# 4 6 9 11  30
# 2 28

# month = int(input())
# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print(31)
# elif month in [4, 6, 9, 11]:
#     print(30)
# else:
#     print(28)


# weight = int(input())

# if weight < 60:
#     print('Легкий вес')
# elif weight < 64:
#     print('Первый полусредний вес')
# elif weight < 69:
#     print('Полусредний вес')


# a = int(input())
# b = int(input())
# operation = input()

# if operation == '+':
#     print(a + b)
# elif operation == '-':
#     print(a - b)
# elif operation == '*':
#     print(a * b)
# elif operation == '/':
#     if b == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(a / b)
# else:
#     print("Неверная операция")


# color1 = input()
# color2 = input()

# if color1 not in ("красный", "синий", "желтый") or color2 not in ("красный", "синий", "желтый"):
#     print("ошибка цвета")
# else:
#     if color1 == color2:
#         print(color1)
#     elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
#         print("фиолетовый")
#     elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
#         print("оранжевый")
#     elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
#         print("зеленый")


# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# left = max(a1, a2)  
# right = min(b1, b2) 

# if left > right:
#     print("пустое множество")
# elif left == right:
#     print(left)  
# else:
#     print(left, right) 


# number = int(input())

# print('YES' if number % 100 == 00 else 'NO')


# numb1, numb2, numb3, numb4 = int(input()), int(input()), int(input()), int(input())

# if (numb1 + numb2) % 2 == (numb3 + numb4) % 2:
#     print('YES')
# else:
#     print('NO')


# age = int(input())
# sex = input()

# if 10 <= age <= 15 and sex == 'f':
#     print('YES')
# else:
#     print('NO')



# x1 = int(input())
# y1 = int(input())


# x2 = int(input())
# y2 = int(input())

# if abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")


# Ход слона

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
#     print('YES')
# else:
#     print('NO')


# Ход коня

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# difference_product = (x1 - x2) * (y1 - y2)

# if difference_product == 2 or difference_product == -2:
#     print("YES")
# else:
#     print("NO")
    

# Ход ферзя

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if x1 == x2 or y1 == y2 or (y1 - y2) ** 2 == (x1 - x2) ** 2:
#     print("YES")
# else:
#     print("NO")
    

