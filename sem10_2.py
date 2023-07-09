'''Задание №2
📌 Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании экземпляра.
📌 У класса должно быть два метода, возвращающие периметр и площадь.
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.'''


class Rangler:

    def __init__(self, length, winght=None):
        self.length = length
        self.winght = length if winght is None else winght

    def perim(self) -> int:
        return round(2 * (self.length + self.winght), 2)

    def squer(self) -> int:
        return round(self.length * self.winght, 2)


if __name__ == '__main__':
    rang = Rangler(4.19, 15.23)
    print(f'Периметр: {rang.perim()}, площадь: {rang.squer()}')
