""" Задание 1"""
my_int = 4
print(type(my_int))

my_float = 1.5
print(type(my_float))

a = input ("Введите число:")
print(a)

number = int(input('Введите число от 0 до 100: '))
while number >= 100 or number < 0:
number = int(input('Введите число от 0 до 100: '))
print('Число введено корректно')

real_name = 'Яковлева Т.А'
p = input('Введите ФИО:')
if p == real_name:
print('Добро пожаловать!')

""" Задание 2"""
seconds = int(input ('Введите значение в секундах:'))
minutes = seconds // 60
hours = minutes // 60

print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

""" Задание 3"""
number = input('Введите число n: ')
comp = int(number) + int(number + number) + int(number + number + number)
print('Итоговая сумма:', comp)

""" Задание 4"""

p = int(input('Введите положительное число:'))
Max = int(p % 10)
p = int(p / 10)

while p > 0:
if int(p % 10) > Max:
Max = int(p % 10)
p = int(p / 10)
print('Наибольшее число:', Max)

""" Задание 5"""

p = float(input("Введите выручку фирмы "))
c = float(input("Введите издержки фирмы "))
if p > c:
    print(f"Фирма работает с прибылью. Рентабельность выручки {p / c:.2f}")
    w = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника  {p / w:.2f}")
elif p == c:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

""" Задание 6"""
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите желаемый результат в км "))

result_day = 1
print(result_day,"-й день: ",a)

while a < b:
   a = a + (0.1 * a)
   result_day += 1
   print(result_day,"-й день: %.2f" % a)
print("Вы достигнете желаемых показателей на %.d день" % result_day)