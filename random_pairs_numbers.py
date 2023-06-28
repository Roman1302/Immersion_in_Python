'''✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.'''
import os
from random import randint, uniform

MIN = -1000
MAX = 1000


def pairs_nume(count_row, filename, dir):
    if dir == '':
        os.getcwd()
    else:
        os.chdir(dir)
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for _ in range(count_row):
                f.write(f'{randint(MIN, MAX)}|{round(uniform(MIN, MAX), 2)}\n')


if __name__ == '__main__':
    dir = "tyu"
    if not os.path.exists(dir):
        os.mkdir(dir)
    pairs_nume(5, 'numes.txt', dir)
