'''Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.'''

import random

MIN_RAND = -100_000
MAX_RAND = 100_000

companies = ['Росинка',
             'Заря',
             'Октябрь',
             'Альтернатива',
             'Сибирь']


def random_income(comp):
    r_i = {}
    for i in range(len(comp)):
        numbers = []
        for _ in range(len(comp[i])):
            numbers.append(random.randint(MIN_RAND, MAX_RAND))
        r_i[comp[i]] = numbers
    return r_i


def check(rep):
    for i in range(len(rep)):
        for _ in range(len(list(rep)[i])):
            total = sum(rep.get(list(rep)[i]))
            if total > 0:
                meaning = True
            else:
                meaning = False
    return meaning


print(random_income(companies))
print(check(random_income(companies)))
