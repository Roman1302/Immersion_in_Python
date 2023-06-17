'''Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.'''
from random import randint

LIST_LENGTH = 20
MIN_RAND = 0
MAX_RAND = 9


def random_list(length, min, max):
    numbers = []
    for _ in range(length):
        numbers.append(randint(min, max))
    return numbers


def cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    if li_copy[0] < 0:
        li_copy[0] = 0
    if li_copy[1] > LIST_LENGTH:
        li_copy[1] = LIST_LENGTH + 1
    return li_copy


def amount_gap(ind):
    am_gap = 0
    for i in range(ind[0], ind[1] - 1):
        am_gap += random_num[i]
    return am_gap


print(f"Программа работы со списком\n")

random_num = random_list(LIST_LENGTH, MIN_RAND, MAX_RAND)
print(f'Случайный список    {random_num}')

indexes_0 = [int(x) for x in input("Введите два индекса через пробел: ").split()]

indexes = cloning(indexes_0)

print(f'Cумму чисел между переданными индексами {indexes_0} = {amount_gap(indexes)}')
