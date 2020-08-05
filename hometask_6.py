# Task 1
# Создать класс TrafficLight (светофор) и определить у него
# один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Цвет светофора : \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

# Task 2
# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
         return self._length * self._width * self._volume


class RealMass(Road):
    def __init__(self, _length, _width, _volume):
        super().__init__(_length, _width)
        self._volume = _volume


r = RealMass(20, 5000, 125)
print(r.mass())

# Task 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__get_full_name(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
         return self.name, self.surname

    def get_total_income(self):
        return int(self._income.get('wage')) + int(self._income.get('bonus'))


total = Position('Ivan', 'Petrov', 'Engineer', '70000', '15000')
print(total.get_full_name())
print(total.position)
print(total.get_total_income())

#Task 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
         return  f'{self.name} начала движение'
    def stop(self):
         return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула налево'

    def turn_left(self):
        return f'{self.name} повернула напрво'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'

        if self.speed > 60:
          return f'Скорость автомобиля {self.name} выше разрешенной скорости'
        else:
          return f'Скорость автомобиля {self.name} в рамках разрешенной скорости'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'
        if self.speed > 40:
         return f'Скорость автомобиля {self.name} выше разрешенной скорости'

        else:
            return f'Скорость автомобиля {self.name} в рамках разрешенной скорости'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Машина {self.name} из полицейского участка'
        else:
            return f'Машина {self.name} не из полицейского участка'


porsche = SportCar(120, 'Красная', 'Porsche', False)
kia = TownCar(60, 'Черная', 'KIA RIO', False)
lada = WorkCar(30, 'Металик', 'Lada', False)
ford = PoliceCar(110, 'Белая',  'Ford', True)
print(lada.turn_right())
print(f'Когда {kia.turn_right()},{porsche.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'{lada.name} цвет - {lada.color}')
print(f'Является {kia.name} полицейской машиной ? {kia.is_police}')
print(f'Является {ford.name} полицейской машиной ? {ford.is_police}')
print(kia.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())

# Task 5 Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}.Запуск отрисовки ручкой'
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}.Запуск отрисовки карандашом'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}.Запуск отрисовки маркером'
pen = Pen('ручку')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())