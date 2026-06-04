# Продолжение
# ТЕМА 6 (6.2)


# part1 = '"Python is a great language!", said Fred. '
# part2 = '"I don\'t ever remember having this much fun before."'
# result = part1 + part2
# print(result)


# first_name = input()
# last_name = input()

# print("Hello " + first_name + " " + last_name + "! You have just delved into Python")


# club = input()

# print(f'Футбольная команда {club} имеет длину {len(club)} символов')


# city1 = input()
# city2 = input()
# city3 = input()

# if len(city1) > len(city2) > len(city3):
#     print(city3)
#     print(city1)
# elif len(city3) > len(city2) > len(city1):
#     print(city1)
#     print(city3)
# elif len(city1) > len(city3) > len(city2):
#     print(city2)
#     print(city1)
# elif len(city3) > len(city1) > len(city2):
#     print(city2)
#     print(city3)
# elif len(city2) > len(city1) > len(city3):
#     print(city3)
#     print(city2)
# elif len(city2) > len(city3) > len(city1):
#     print(city1)
#     print(city2)


# string = input()
# if 'синий' in string:
#     print('YES')
# else:
#     print('NO')


# a = input()
# if 'суббота' in a or 'воскресенье' in a:
#     print('YES')
# else:
#     print('NO')


# a = input()
# if '@' in a and '.' in a:
#     print('YES')
# else:
#     print('NO')


# # ТЕМА 7


# for i in range(10):
#     print('Python is awesome!')


# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')


# string = input()
# count = int(input())
# for i in range(count):
#     print(string)


# n = int(input())
# for i in range(n):
#     print('*' * 19)


# string = input()
# for i in range(10):
#     print(i, string)


# n = int(input())
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)


# n = int(input())
# for i in range(n):
#     print('*' * (n - i))


# m = int(input())  
# p = int(input())  
# n = int(input())  

# factor = 1 + p / 100

# for day in range(1, n + 1):
#     population = m * (factor ** (day - 1))
#     print(day, population)


# m = int(input())
# n = int(input())
# for i in range(m, n +1):
#     print(i)


# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)


# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)


# m = int(input())
# n = int(input())

# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)


# m = int(input())
# n = int(input())
# if m > n:
#     for i in range(m, n - 1, - 1):
#         print(i)
# else:
#     for i in range(m, n + 1):
#         print(i)


# prod = 1
# for i in range(-7, -3, 1):
#     if i < -5:
#         prod = prod * i

# print(prod)


# a = int(input())
# b = int(input())
# count = 0

# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         count += 1
# print(count) 


# n = int(input())
# count = 0
# for i in range(n):
#     s = int(input())
#     count += s
# print(count)


# import math

# n = int(input())

# # Вычисляем сумму 1/1 + 1/2 + ... + 1/n
# total = 0
# for i in range(1, n + 1):
#     total += 1 / i

# # Вычисляем результат
# result = total - math.log(n)

# print(result)


# n = int(input())
# count = 1
# for i in range(1, n + 1):
#     count *= i
# print(count)

# count = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         count *= n
# print(count)


# n = int(input())
# count = 0
# summa = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
#         summa += i
# print(summa)

# count = 0
# for i in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         count += 1
# if count == 10:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# summa = 1
# for i in range(2, n + 1):
#     if i % 2 == 0:
#         summa -= i
#     else:
#         summa += i
# print(summa)


# n = int(input())
# high = 0
# medium = 0
# for i in range(n):
#     s = int(input())
#     if s > high:
#         medium = high
#         high = s
#     elif s > medium:
#         medium = s
# print(high)
# print(medium)


# n = int(input())
# f1 = 0
# f2 = 1
# for i in range(0, n):
#     f1, f2 = f2, f1 + f2
#     print(f1, end=' ')

# num = int(input())
# total = 0

# while num > -4:
#     num = int(input())
#     total += num
# print(total)


# word = input()
# while word != 'КОНЕЦ':
#     print(word)
#     word = input()


# word = input()
# count = 0
# while word != 'стоп' and word != 'хватит' and word != 'достаточно':
#     count += 1
#     word = input()

# print(count)


# numb = int(input())
# cnt = 0
# while numb >= 0:
#     cnt += numb
#     numb = int(input())
# print(cnt)


# numb = int(input())
# cnt = 0
# while numb > 0 and numb < 6:
#     if numb == 5:
#        cnt += 1
#     numb = int(input()) 
# print(cnt)


# name = input()
# while '_' in name:
#     name = input()
# print(name)


# name = input()
# save_name = ''
# cnt = -1
# while name != 'Александра':
#     name = input()
# while name != 'Левон':
#     name = input()
#     cnt += 1
# print(cnt)


