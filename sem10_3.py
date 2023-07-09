'''Задание №3
📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.'''


class Human:

    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1
        return self.__age

    def full_name(self):
        print(f'{self.first_name} {self.last_name} ')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.get_age()} {self.gender} '


if __name__ == '__main__':
    fio1 = Human('Петя', 'Иванов', 21, 'м')
    fio2 = Human('Иван', 'Петров', 24, 'м')
    fio3 = Human('Катя', 'Сидорова', 18, 'ж')
    print(fio1)
    print(fio2)
    print(fio3)
    fio1.birthday()
    fio2.birthday()
    fio1.birthday()
    print(fio1)
    print(fio2)
    print(fio3)
