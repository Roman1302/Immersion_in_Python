'''✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.'''
from random import randint

print("Программа вывода порядковых номеров нечётных элементов списка\n")

LIST_LENGTH = 20
MIN_RAND = 1
MAX_RAND = 100

numbers = []
for i in range(LIST_LENGTH):
    numbers.append(randint(MIN_RAND, MAX_RAND))
print(f'Случайный список    {numbers}\n')

complect = []
step = 0
while step < len(numbers):
    if numbers[step] % 2 != 0:
        complect.append(step + 1)
    step += 1
print(f'Номера нечетных чисел: {complect}')
