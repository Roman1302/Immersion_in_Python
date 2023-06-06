'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.'''

from random import randint

print("Программа проверки треугольника")

a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
print(a, b, c)

if a == b == c:
    print("равносторонний")

elif (a == b and (a+b) > c) or (b == c and (b+c) > a) or (a == c and (a+c) > b):
    print("Равнобедренный")

elif (a+b) > c and (b+c) > a and (a+c) > b:
    print("Разносторонний")

else:
    print("не существует")