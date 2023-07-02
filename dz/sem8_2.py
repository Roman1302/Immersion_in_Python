'''Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.'''
import json
import os.path


def funk(file_json='access_level.json'):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            f1 = json.load(f)
    else:
        f1 = {str(i): {} for i in range(1, 8)}

    while True:
        data = input('Введите через пробел имя, ID, уровень доступа: ')
        if not data:
            break
        user_input, id, access = data.split()
        if id not in f1[access]:
            f1.setdefault(access, {id: user_input})[id] = user_input

        with open(file_json, 'w', encoding='utf-8') as f:
            json.dump(f1, f, ensure_ascii=False)


if __name__ == '__main__':
    funk('sdfg.json')
