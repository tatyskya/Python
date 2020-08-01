# Task 1 Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
my_file = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()

# Task 2
# Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_file = open('Brod.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('Brod.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('Brod.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('Brod.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

# Task 3 Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.
with open('sal.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

#  Task 4 Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('numb.txt', 'r') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('numb.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)