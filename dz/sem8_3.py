'''Переобразование из json в csv'''
import csv
import json


def json_csv(json_f, csv_f='csv_test.csv'):
    with (open(json_f, 'r', encoding='utf-8') as j_f,
          open(csv_f, 'w', encoding='utf-8', newline='') as c_f):
        json_dect = json.load(j_f)
        rows = []
        for level, in_dect in json_dect.items():
            for id, name in in_dect.items():
                rows.append({'level': int(level), 'id': id, 'name': name})
        c_write = csv.DictWriter(c_f, fieldnames=['level', 'id', 'name'])
        c_write.writeheader()
        c_write.writerows(rows)


if __name__ == '__main__':
    json_ = 'sdfg.json'
    csv_ = 'csv.csv'
    json_csv(json_, csv_)
