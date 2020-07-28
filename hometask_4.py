
# Task 1 Вариант 1
def salary(production, rate, reward):

    return production * rate + reward


print(f'Результат - {salary(int(input("Введите выработку в часах : ")), int(input("Введите ставку в часах :")), int(input("Введите премию :")))}')

# Task 1 Вариант2
import sys


print("Выработка в часах : {} Ставка :  {} Премия : {}".format(sys.argv[0], sys.argv[2], sys.argv[3]))
print('Total value=',(int(sys.argv[0])*int(sys.argv[2]) + int(sys.argv[3])))

# #Task 2 Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить
# в виде списка. Для формирования списка использовать генератор.
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(my_list)
print(new_list)

# Task 3 Вывести числа кратные 20 или 21
print(f'Числа от 20 до 240 кратные 20 или 21 : - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

Task 4 Вычленить уникальные значения
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

# # Task 5 Вывести произведение четных чисел от 100 до 1000

from functools import reduce
def numb(arg, el):
    return arg * el

print(f'Список чисел от 100 до 1000: - {[el for el in range(99, 1000) if el % 2 == 0]}')
print(f'Произведение чисел от 100 до 1000: - {reduce(numb, [el for el in range(99, 1000) if el % 2 == 0])}')

# Task 6 Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


from itertools import cycle
my_list = [1, 23, 365, 45, 100]
for el in cycle(my_list):
    if el > 250:
        break
    print(el)
# Task 7 Просчитать факториал чисел
from itertools import count
from math import factorial

def generator():
    for el in count(1):
        yield factorial(el)

gen = generator()
x = 0
for i in gen:
    if x < 10:
        print(i)
        x += 1
    else:
        break