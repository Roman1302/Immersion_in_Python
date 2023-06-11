'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''

print("Программа перевода в шестнадцатеричную систему")

num = -1
while num < 0 or num > 1000000:
    try:
        num = int(input('Введите число от 1 до 1000000: '))
    except:
        print('Введите число')

dict_hex = {10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'}
list_hex = []
calculation = num

while (calculation // 16) > 0:
    ostatok = calculation % 16
    if ostatok > 9:
        list_hex.insert(0, dict_hex[ostatok])
    else:
        list_hex.insert(0, str(ostatok))
    calculation = calculation // 16
list_hex.insert(0, str(calculation))

print(f'Число {num} в шестнатиричной системе счисления обозначается: {("".join(list_hex))}')
print(f'Проверка: {num} в шестнатиричной системе с помощью hex: {hex(num)}')
