'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.'''

import random
MAXIMUM_WEIGHT = 20

numbers = []
for i in range(9):
    sampl = numbers.append(int(random.random() * 100) / 10)

fruits = ['вещь_1', 'вещь_2', 'вещь_3', 'вещь_4', 'вещь_5', 'вещь_6', 'вещь_7', 'вещь_8', 'вещь_9']

dict_thing = dict(zip(fruits, numbers))
print(dict_thing)

print(f'Максимальная грузоподъемность рюкзака = {MAXIMUM_WEIGHT}')

complect = []
weight_compl = 0
step = 0

while step < len(dict_thing) and weight_compl + list(dict_thing.values())[step] <= MAXIMUM_WEIGHT:
    weight_compl = weight_compl + list(dict_thing.values())[step]
    complect.append(list(dict_thing)[step])
    step += 1

print(f'\nВ рюкзак влезет: {", ".join(complect)} ')
print(f'Масса вещей = {weight_compl}')
