'''Домашнее задание
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.'''

from pathlib import Path
import csv
import json
import pickle
import os


def get_dir_size(path='.'):
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result


def direct_info(direct):
    if direct == '':
        direct = os.getcwd()

    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with open('direct_info.json', 'w') as f_json, \
            open('direct_info.csv', 'w', newline='', encoding='utf-8') as f_csv, \
            open('direct_info.pickle', 'wb') as f_pickle:
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            if dir_name == []:
                os.chdir(dir_path)
                for fi in file_name:
                    json_data[dir_path].update({fi: {'size': os.path.getsize(fi), 'file_or_dir': 'file'}})
                    rows.append({'name': fi, 'path': dir_path, 'size': os.path.getsize(fi),
                                 'file_or_dir': 'file'})
            else:
                for dir in dir_name:
                    json_data[dir_path].update({dir: {'size': os.path.getsize(dir), 'file_or_dir': 'directory'}})
                    rows.append(
                        {'name': dir, 'path': dir_path, 'size': os.path.getsize(dir), 'file_or_dir': 'directory'})
                for fi in file_name:
                    json_data[dir_path].update({fi: {'size': os.path.getsize(fi), 'file_or_dir': 'file'}})
                    rows.append({'name': fi, 'path': dir_path, 'size': os.path.getsize(fi),
                                 'file_or_dir': 'file'})
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


if __name__ == '__main__':
    direct_info(os.getcwd())
