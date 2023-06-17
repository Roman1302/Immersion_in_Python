'''Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.'''
import sys

print("Программа Банкомат")


class card:
    SUM = 0
    ACTION = 0
    MULTIPLICITY_REPLENISHMENT = 50
    WITHDRAWAL_FEE = 0.015
    DIVIDENDS = 0.03
    NUMBER_OPERATIONS = 3
    LUXURY_COMMISSION = 0.1
    SUM_LUXURY = 5_000_000
    MINIMUM_COMMISSION = 30
    MAXIMUM_COMMISSION = 600


def replenishment():
    money = int(input('Введите сумму пополнения, кратную 50: '))
    if money % card.MULTIPLICITY_REPLENISHMENT == 0:
        card.SUM += money
        print(f'Вы пополнили счет на {round(money, 2)} у.е. ')
        card.ACTION += 1.
    else:
        print('Сумма пополнения не кратно 50 у.е.')


def bonus():
    bonus_sum = card.SUM * card.DIVIDENDS
    card.SUM += card.SUM * card.DIVIDENDS
    print(f'начислен бонус {round(bonus_sum, 2)} y.e.')


def withdrawal():
    money = int(input('Введите сумму снятия, кратную 50: '))
    if money % card.MULTIPLICITY_REPLENISHMENT == 0:
        if money * card.WITHDRAWAL_FEE < card.MINIMUM_COMMISSION:
            rate = card.MINIMUM_COMMISSION
        elif money * card.WITHDRAWAL_FEE > card.MAXIMUM_COMMISSION:
            rate = card.MAXIMUM_COMMISSION
        else:
            rate = money * card.WITHDRAWAL_FEE
        if card.SUM - money - rate < 0:
            print("Отказано, недостаточно средств")
        else:
            card.SUM = card.SUM - money - rate
            print(f'Вы сняли со счета {round(money, 2)} y.e. и проценты за снятие {round(rate, 2)} у.е.')
            card.ACTION += 1
    else:
        print('Сумма снятия не кратна 50.')


while True:
    print(f'Cумма на счете составляет {round(card.SUM, 2)} у.е.')
    operation = int(input("Выбирите действие: 1-Пополнить, 2-Снять, 3-Выйти: "))
    if card.SUM > card.SUM_LUXURY:
        TAX = card.SUM * card.LUXURY_COMMISSION
        card.SUM -= TAX
        print(
            f'С вас списали налог на богатство в размере {round(TAX, 2)} y.e. Сумма на счёте {round(card.SUM, 2)} y.e.')

    if operation == 1:
        replenishment()
    if operation == 2:
        withdrawal()
    if operation == 3:
        print(f'Сумма на счёте {round(card.SUM, 2)} y.e.')
        sys.exit()

    if card.ACTION % card.NUMBER_OPERATIONS == 0:
        bonus()
    else:
        pass
