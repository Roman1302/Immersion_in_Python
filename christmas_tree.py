'''Нарисовать в консоли ёлку спросив
у пользователя количество рядов.'''

print("Программа рисования ёлочки")
logic = True

while logic:
    try:
        quantity = int(input("Введите количество рядов у ёлки: "))
        sign = input("Введите любой символ, из которых юудет сделана ёлочка: ")
        for i in range(1, quantity*2, 2):
            print(f'{i*sign:^{quantity*2}}')
        logic = False
    except ValueError:
        logic = True
        print("ОШИБКА!")