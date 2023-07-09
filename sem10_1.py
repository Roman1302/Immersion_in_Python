'''Задание №1
📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.'''
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def lenth_circl(self):
        return round(2 * pi * self.radius, 2)

    def squer_circl(self):
        return round(pi * self.radius * self.radius, 2)


if __name__ == '__main__':
    cir = Circle(3)
    print(f"Длина окружности: {cir.lenth_circl()}, Площадь окружности: {cir.squer_circl()}")
