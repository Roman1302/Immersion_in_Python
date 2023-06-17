'''Создайте функцию генератор чисел Фибоначчи'''


def fibon(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


num = int(input("Введите количество чисел Фибоначчи: "))
print(list(fibon(num)))
