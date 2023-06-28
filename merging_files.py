'''✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.'''
import os
import typing


def read_per_line(file_obj: typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()
    return line[:-1]


def func(dir, names, numbers, results='results.txt'):
    if dir == '':
        os.getcwd()
    else:
        os.chdir(dir)
    with(
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results,
    ):
        len_names = sum(True for _ in f_names)
        len_numbers = sum(True for _ in f_numbers)
        for _ in range(max(len_names, len_numbers)):
            name = read_per_line(f_names)
            num_line = read_per_line(f_numbers)
            int_num, float_num = num_line.split('|')
            int_num, float_num = int(int_num), float(float_num)
            if int_num * float_num > 0:
                a = str(int(int_num * float_num))
                f_results.write(f'{name.upper()}{a}\n')
            if int_num * float_num < 0:
                a = str(abs(int_num * float_num))
                f_results.write(f'{name.lower()}{a}\n')


if __name__ == '__main__':
    dir = "fgh"
    func(dir, 'names.txt', 'numes.txt', 'results.txt')
