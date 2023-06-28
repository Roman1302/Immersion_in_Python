import sys

import creating_folder
import files_with_text
import merging_files
import pseudonyms
import random_pairs_numbers
import renaming_files


def random_pairs_number():
    file_name = input('Введите имя файла с расширением, пример: "numes.txt": ')
    number_pairs_numbers = int(input('Введите количество пар чисел: '))
    dir_name = input("Введите имя папки для размещения файла: ")
    creating_folder.dir(dir_name)
    random_pairs_numbers.pairs_nume(number_pairs_numbers, file_name, dir_name)


def pseudonym():
    file_name = input('Введите имя файла с расширением, пример: "numes.txt": ')
    random_combinations = int(input("Введите количество случайных комбинаций: "))
    dir_name = input("Введите имя папки для размещения файла: ")
    creating_folder.dir(dir_name)
    pseudonyms.pseudonym(random_combinations, file_name, dir_name)


def creat_folder():
    dir_name = input("Введите имя папки для размещения файла: ")
    creating_folder.dir(dir_name)


def files_with_texts():
    number_combinations = int(input("Введите количество файлов: "))
    expansion = input("Введите название расширения для файлов без точки: ")
    dir_name = input("Введите имя папки для размещения файла: ")
    creating_folder.dir(dir_name)
    files_with_text.create_files_with_extension(number_combinations, expansion, dir_name)


def merging_file():
    dir_name = input("Введите имя папки где размещены файлы: ")
    name_num = input("Введите имя файла с парами чисел: ")
    name_pseud = input("Введите имя файла с псевдоименами: ")
    name_res = input("Введите имя файла, куда поместить результат: ")
    merging_files.func(dir_name, name_pseud, name_num, name_res)


def renaming_file():
    dir_name = input("Введите имя папки где размещены файлы: ")
    expansion_old = input("Введите расширения для файлов, которые нужно переименовать, пример: '.txt': ")
    name_new = input("Введите добавочное имя файла: ")
    expansion_new = input("Введите новое расшерение файлов, пример '.100': ")
    renaming_files.reneme_files(expansion_old, name_new, expansion_new, dir_name)



action = int(input("1 - Создать файл с парами чисел\n"
                   "2 - Создать файл с набором псевдоименами\n"
                   "3 - Создать папку\n"
                   "4 - Создать серию файлов с набором текста\n"
                   "5 - Объеденить файлы (пары чисел и псевдоимена)\n"
                   "6 - Переименовать файлы определенного расширения\n"
                   "0 - ВЫХОД\n\n"
                   "Что желаете сделать: "))
if action == 1:
    random_pairs_number()
if action == 2:
    pseudonym()
if action == 3:
    creat_folder()
if action == 4:
    files_with_texts()
if action == 5:
    merging_file()
if action == 6:
    renaming_file()
if action == 0:
    sys.exit()
else:
    pass
