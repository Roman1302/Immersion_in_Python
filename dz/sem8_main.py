import sys

import sem8_1
import sem8_2
import sem8_3
import sem8_4
import sem8_5
import sem8_6
import sem8_dz


def write_json_number():
    file_name = input('Введите путь к файлу с расширением txt c парами: имя и значение, пример: "numes.txt": ')
    json_name = input("Введите имя файла с расширением json для сохранения: ")
    sem8_1.write_json(file_name, json_name)


def access_level():
    file_name = input('Введите имя файла с расширением json, для сохранения результатов, пример: "numes.json": ')
    sem8_2.funk(file_name)


def json_csv():
    json_name = input("Введите имя файла json для преобразования в файл csv: ")
    csv_name = input('Введите имя файла с расширением csv, для сохранения результатов, пример: "numes.csv": ')
    sem8_3.json_csv(json_name, csv_name)


def csv_json():
    csv_name = input("Введите имя файла csv для преобразования в файл json: ")
    json_name = input('Введите имя файла с расширением json, для сохранения результатов, пример: "numes.json": ')
    sem8_4.func(csv_name, json_name)


def json_pickle():
    json_name = input("Введите имя файла json для преобразования в файл pickle: ")
    pickle_name = input('Введите имя файла с расширением pickle, для сохранения результатов, пример: "numes.pickle": ')
    sem8_5.func(json_name, pickle_name)


def pickle_csv():
    pickle_name = input("Введите имя файла pickle для преобразования в файл csv: ")
    csv_name = input('Введите имя файла с расширением csv, для сохранения результатов, пример: "numes.csv": ')
    sem8_6.pickle_csv(pickle_name, csv_name)


def directory_data():
    direct = input("Введите путь директории: ")
    sem8_dz.direct_info(direct)


action = int(input("1 - Приобразование файла txt в json\n"
                   "2 - Создать файл json с параметрами уровня доступа\n"
                   "3 - Переобразование из json в csv\n"
                   "4 - Преобразование csv в json\n"
                   "5 - Преобразование всех файлов json в pickle\n"
                   "6 - Преобразование pickle в csv\n"
                   "7 - Сохранение в файлы csv, json, pickle файлов и папок данной директории\n"
                   "0 - ВЫХОД\n\n"
                   "Что желаете сделать: "))
if action == 1:
    write_json_number()
if action == 2:
    access_level()
if action == 3:
    json_csv()
if action == 4:
    csv_json()
if action == 5:
    json_pickle()
if action == 6:
    pickle_csv()
if action == 7:
    directory_data()
if action == 0:
    sys.exit()
else:
    pass
