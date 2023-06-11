'''Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.'''

from random import randint

LIST_LENGTH = 20
MIN_RAND = 0
MAX_RAND = 9

print(f"Программа работы со списком\n")
numbers = []
for i in range(LIST_LENGTH):
    numbers.append(randint(MIN_RAND, MAX_RAND))
print(f'Случайный список    {numbers}')

# дубликаты
repeats = []
for x in numbers:
    if numbers.count(x) > 1:
        repeats.append(x)
print(f'Дубликаты           {repeats}')

# без повторов
seen = set()
uniq = []
for x in numbers:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
print(f'Список без повторов {uniq}')
