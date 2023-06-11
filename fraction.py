'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.'''

from fractions import Fraction

print("Программа сложения и произведение дробей")

a = (input('Введите первую дробь в виде: "1/2": '))
# a = "11/9"
b = (input('Введите вторую дробь в виде: "1/2": '))
# b="5/66"
numerator_a = int(a.split('/')[0])
denominator_a = int(a.split('/')[1])
numerator_b = int(b.split('/')[0])
denominator_b = int(b.split('/')[1])

# Сложение
numerator_sum = numerator_a * denominator_b + numerator_b * denominator_a
# print(f'numerator_sum {numerator_sum}')
denominator_sum = denominator_b * denominator_a
# print(f'denominator_sum {denominator_sum}')

divider_sum = 0
for i in range(2, int(numerator_sum)):
    if numerator_sum % i == 0 and denominator_sum % i == 0:
        divider_sum = i
        # print(divider_sum)
# print(f'divider_sum {divider_sum}')
if numerator_sum == denominator_sum:
    print(f'{a} + {b} =  1')
elif divider_sum > 1:
    print(f'{a} + {b} =  {int(numerator_sum / divider_sum)}/{int(denominator_sum / divider_sum)}')
else:
    print(f'{a} + {b} = {numerator_sum}/{denominator_sum}')

# Произведение
numerator_com = numerator_a * numerator_b
denominator_com = denominator_a * denominator_b
divider_com = 0
for i in range(2, int(numerator_com)):
    if numerator_com % i == 0 and denominator_com % i == 0:
        divider_com = i
# print(f'divider_com {divider_com}')
if numerator_com == denominator_com:
    print(f'{a} * {b} =    1')
elif divider_com > 1:
    print(f'{a} * {b} =  {int(numerator_com / divider_com)}/{int(denominator_com / divider_com)}')
else:
    print(f'{a} * {b} =  {numerator_com}/{denominator_com}')

print(f'\nПроверка с помощью fractions:')
print(f"{a} + {b} =  {Fraction(numerator_a, denominator_a) + Fraction(numerator_b, denominator_b)}")
print(f"{a} * {b} =   {Fraction(numerator_a, denominator_a) * Fraction(numerator_b, denominator_b)}")
