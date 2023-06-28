'''Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.
* При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>'''
import os


def new_name_generator(name, count, new_name, new_extension):
    temp_number = []
    temp_count = list(str(count))
    number = []
    i = 0
    j = 0
    while i < len(temp_count):
        number.append(temp_count[i])
        i += 1
    while j < (len(temp_number) - i):
        number.insert(0, temp_number[j])
        j += 1
    number_string = ""
    for char in number:
        number_string += str(char)

    t_n = name.split(".")[0]

    tem_new_name = t_n + new_name + number_string + new_extension
    return tem_new_name


def reneme_files(extension, new_name, new_extension, dir):
    # print(os.listdir(path))
    all_files = os.listdir(os.chdir(dir))
    files_for_rename = []
    for file in all_files:
        if file.endswith(extension):
            files_for_rename.append(file)

    count = 1
    for file in files_for_rename:
        os.rename(file, new_name_generator(file, count, new_name, new_extension))
        count += 1


if __name__ == '__main__':
    dir = 'qwe'
    reneme_files('.test', '_TEST_', '.100', dir)
# path=os.chdir(