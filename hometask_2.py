# # Task 1 (Создать список и заполнить его элементами различных типов данных)
# my_list = ['name', 5, 2.5, 6, 'text']
# for elem in my_list:
#         print(type(elem))

#Task 2 (Поменять местами объекты списка)
my_list = []

list_count = int(input('Введите кол-во объектов в списке'))

while len(my_list) < list_count:
    my_list.append((input('Введите %d элемент списка' % (len(my_list)+1))))

i=0
if len(my_list) % 2 == 0:
    while i < len(my_list):
        if(i >= len(my_list)):
            break
        else:
            buffer = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = buffer
            i+=2
elif len(my_list) % 2 != 0:
    while i < len(my_list):
        if(len(my_list) == 1):
            break
        elif(i == (len(my_list)-1)):
            break
        else:
            buffer = my_list[i]
            my_list[i]=my_list[i+1]
            my_list[i+1]=buffer
            i=i+2

for i in range(len(my_list)):
    print('%d элемент списка = ' % i,my_list[i])
#
# # Task 3 Вариант 1 (Ввести месяц и определить время года)
# my_list = ['зима', 'весна', 'лето', 'осень']
# month = int(input('Введите целое число от 1 до 12:'))
# if month == 12 or month == 1 or month == 2:
#     print('время года',my_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print('время года',my_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print('время года',my_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print('время года',my_list[3])
#
# # Task 3 Вариант 2 (Ввести месяц и определить время года)
# seasons = {'Зима': (12, 1, 2),
#            'Весна': (3, 4, 5),
#            'Лето': (6, 7, 8),
#            'Осень': (9, 10, 11)}
# month = int(input('Введите целое число от 1 до 12:'))
# for key in seasons.keys():
#     if month in seasons[key]:
#         print(key)
# # Task 3 Вариант 3
# my_list = ['зима','зима','весна','весна','весна', 'лето','лето','лето', 'осень', 'осень', 'осень','зима']
# print('Ваше время года - ', my_list[int(input('Введите целое число от 1 до 12:')) -1])
#
# # Task 4 (Внесение словосочетания с разделением на строки)
# my_word = (input('Введите словосочетание:'))
# for i, elem in enumerate(my_word.split(), 1):
#     print(i, elem[0:10])
#
# # Task 5 (Внесение в рейтинг значений)
# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# variable = int(input('Введите новый элемент рейтинга:'))
# my_list.append(variable)
# my_list.sort(key=None, reverse=True)
# print(f"новый рейтинг - {my_list}")
#
# # Task 5 (Внесение в рейтинг значений с выполнением условия подстановки)
# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# variable = int(input('Введите новый элемент рейтинга:'))
# i=0
# for i in range(len(my_list)):
#     if i == 0 and my_list[i] < variable:
#         my_list.insert(0, variable)
#         break
#     elif i == (len(my_list) -1) and my_list[i] > variable:
#         my_list.append(variable)
#         break
#     elif i != (len(my_list) -1) or i != 0:
#             if my_list[i] >= variable > my_list[i + 1]:
#                 my_list.insert(i+1, variable)
#                 break
# print(f"новый рейтинг - {my_list}")









