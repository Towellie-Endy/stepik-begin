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


m = int(input())
p = int(input())
n = int(input())
rez = m + (p / 100)
ans = rez
print(ans)
for i in range(n):
    rez += ans + (p / 100)
    print(i + 1, rez)