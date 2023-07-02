'''Приобразование файла txt в json'''
import json
import os


def write_json(name, output='output_test.json'):
    # os.chdir(dir)
    with(open(name, 'r', encoding='utf-8') as res,
         open(output, 'w', encoding='utf-8') as j):
        dict_res = dict()
        for item in res:
            key, value = item.replace('\n', '').split('_')
            dict_res[key.capitalize()] = value
        json.dump(dict_res, j, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    # dirs="/home/rom/PycharmProjects/PY/sem7/tyu"
    write_json('/home/rom/PycharmProjects/PY/sem7/tyu/results.txt', 'output.json')
