'''Задание №4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь '''

from random import randint
from sem10_3 import Human


class Sotrudnik(Human):

    def __init__(self, first_name: str, last_name: str, age: int, gender: str, prof: str):
        self.prof = prof
        self.id = self._get_id()
        self.level = self._secr_level()
        super().__init__(first_name, last_name, age, gender)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.get_age()} {self.gender}  {self.prof} {self.id}  {self.level}'

    def _get_id(self) -> int:
        MIN_ID = 100000
        MAX_ID = 1000000
        return randint(MIN_ID, MAX_ID)

    def _secr_level(self) -> int:
        id = self._get_id()
        sum = 0
        for i in list(str(id)):
            sum += int(i)
        res_level = sum % 7
        return res_level


if __name__ == '__main__':
    fio_sotr1 = Sotrudnik('Петя', 'Иванов', 21, 'м', 'povar')
    fio_sotr2 = Sotrudnik('Иван', 'Петров', 24, 'м', 'strip')
    fio_sotr3 = Sotrudnik('Катя', 'Сидорова', 18, 'ж', 'teacher')
    print(fio_sotr1)
    print(fio_sotr2)
    print(fio_sotr3)
