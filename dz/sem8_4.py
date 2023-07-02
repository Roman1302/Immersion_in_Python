'''Преобразование csv в json'''
import csv
import json


def func(csv_, json_='csv_json.json'):
    with(open(csv_, 'r', encoding='utf-8') as c_f,
         open(json_, 'w', encoding='utf-8') as j_f):
        file = [*csv.reader(c_f)]
        headers_lev, headers_id, headers_name = file[0]
        lst = []
        for level, id, name in file[1:]:
            lst.append({headers_lev: level, headers_id: id, headers_name: name, 'hash': hash(name + id)})
        json.dump(lst, j_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    func('csv.csv', "asfgh_new.json")
