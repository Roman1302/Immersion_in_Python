'''Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''

file_abs = "/home/rom/PycharmProjects/PY/5sem_1z.py"


def path_name(name):
    full_file_name = file_abs.split('/')[-1:][0]
    full_path = file_abs.split(full_file_name)[0]
    exten_file = full_file_name.split('.')[-1:][0]
    return (full_path, full_file_name, exten_file)


res_out = path_name(file_abs)
print(res_out)
