# Task 1 Произвести деление 2 чисел с учетом деления на 0
def numbers():
    try:
        arg_1 = float(input('Введите число 1:'))
        arg_2 = float(input('Введите число 2:'))
        final_result = arg_1 / arg_2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "На 0 делить нельзя !"

    if arg_2 != 0:
        return arg_1 / arg_2

    else:

        print('на 0 делить нелья !')


final_result = numbers()
print(final_result)

# Task 2 Создать функцию, которая будет выводить именованные аргументы

def personal_data(name, surname, city, year, phone, mail):

    print(name,', ', surname,', ',city,', ', year,', ' , phone,', ',mail)
personal_data(name='Tanya', surname='Yakovleva', city='Moscow', year='1997', phone='89100135634', mail='bk@mail.ru')

# Task 3 Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов

my_args = []
while len(my_args) < 3:
     my_args.append(int(input('Введите %d аргумент:' % (len(my_args)+1))))

def summ_args():
    res = 0
    my_args.remove(min(my_args))
    for i in my_args:
        res+=i
    return
    print('Сумма элементов =', res)

summ_args()


# Task 4.1 Возведение число x в степень -y

def my_func(x, y):
    return x ** y
print(f'Результат - {my_func(int(input("Введите число x: ")), int(input("Введите целое отрицательное число y:")))}')

# Task 4.2 Возведение число x в степень -y


x = int(input("Введите число x: "))
y = int(input("Введите целое отрицательное число y:"))

def my_func(x, y):

    res=1

    y = -y
    for i in range(y):
        res *= x

    return 1/res



print(f'Результат - ', my_func(x,y))


# Task 5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме

def special_sum ():
        sum_result = 0
        ex = False
        while ex == False:
            numbers = (input('Введите числа или Q для выхода - ').split())

            result = 0
            for el in range(len(numbers)):
                if numbers[el] == 'q' or numbers[el] == 'Q':
                    ex = True
                    break
                else:
                    result = result + int(numbers[el])

            sum_result = sum_result + result
            print(f'Текущая сумма составляет: {sum_result}')
        print(f'Итоговая сумма составляет: {sum_result}')

special_sum()

# Task 6 Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой

def int_func ():
    word = input("Введите слово: ")
    print(word.title())
    return
int_func()
