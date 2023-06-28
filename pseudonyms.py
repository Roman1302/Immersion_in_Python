'''✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.'''

import os
from random import choice, randint

VOVELS = 'eyuioa'
CONSONANT = 'qwertyuiopasdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGTH = 7


def pseudonym(count_names, filename, dir):
    if dir == '':
        os.getcwd()
    else:
        os.chdir(dir)
    if not os.path.exists(filename):
        names = []
        for _ in range(count_names):
            len = randint(MIN_LENGTH, MAX_LENGTH)
            name = []
            letter = choice(VOVELS)
            name.append(letter)
            for _ in range(len - 1):
                name.append(choice(CONSONANT))
            name = ''.join(name).capitalize()
            # print(f'{name = }')
            names.append(name)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(names))





if __name__ == '__main__':
    dir("name_folder")
    pseudonym(10, "filename.txt", "name_folder")
    print("Текущая деректория:", os.getcwd())
