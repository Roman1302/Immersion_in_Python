'''Задание №6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.'''

import csv
import pickle


def pickle_csv(pik_f, csv_f='pickle_csv.csv'):
    with (open(pik_f, 'rb') as p_f,
          open(csv_f, 'w', encoding='utf-8', newline='') as c_f):
        pik_dect = pickle.load(p_f)
        rows = []
        for level, in_dect in pik_dect.items():
            for id, name in in_dect.items():
                rows.append({'level': int(level), 'id': id, 'name': name})
        c_write = csv.DictWriter(c_f, fieldnames=['level', 'id', 'name'])
        c_write.writeheader()
        c_write.writerows(rows)


if __name__ == '__main__':
    pik_ = 'sdfg.pickle'
    vsc_ = 'csv1.csv'
    pickle_csv(pik_, vsc_)
