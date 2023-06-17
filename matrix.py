'''Напишите функцию для транспонирования матрицы.'''


def transporation(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
    return table2


matrix = [["ф", "ы", "в"], [4, 5, 6]]
print(f'Начтальный вид: \n{matrix}')

print(f'Транспонированный вид: \n{transporation(matrix)}')
