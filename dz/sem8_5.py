'''Преобразование всех файлов json в pickle'''

import json
import os
import pickle


def func(dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), 'r', encoding='utf-8') as f,
              open(os.path.join(dir_, json_file.removesuffix('.json') + '.pickle'), 'wb') as f_p):
            pickle.dump(json.load(f), f_p)


if __name__ == '__main__':
    func(os.getcwd())
    with open("asfgh_new.pickle", 'rb') as f_pi:
        print(pickle.load(f_pi))
