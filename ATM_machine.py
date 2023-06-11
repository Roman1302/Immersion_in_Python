'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

print("Программа Банкомат")
sum = 0
action = 0
MULTIPLICITY_REPLENISHMENT = 50
WITHDRAWAL_FEE = 0.015
DIVIDENDS = 0.03
NUMBER_OPERATIONS = 3
LUXURY_COMMISSION = 0.1
SUM_LUXURY = 5_000_000
MINIMUM_COMMISSION = 30
MAXIMUM_COMMISSION = 600

while True:
    operation = int(input("Выбирите действие: 1-Пополнить, 2-Снять, 3-Выйти: "))

    if action == 0:
        print("Банкоман готов к работе.")
    elif action % NUMBER_OPERATIONS == 0:
        print(f"Начисленны % = {round(sum * DIVIDENDS, 2)} у.е. Всего на счете {round(sum + sum * DIVIDENDS, 2)} у.е.")
        sum += sum * DIVIDENDS

    while operation == 1:
        replenishment = int(input("Введите сумму пополнения кратно 50: "))
        if replenishment > SUM_LUXURY:
            sum += replenishment - replenishment * LUXURY_COMMISSION
            action += 1
            print(f"Остаток средств {round(sum, 2)} у.е.")
            operation = False
        elif replenishment % MULTIPLICITY_REPLENISHMENT == 0:
            sum += replenishment
            action += 1
            print(f"Остаток средств {round(sum, 2)} у.е.")
            operation = False
        else:
            operation == 1
            print(f"Остаток средств {round(sum, 2)} у.е.")

    while operation == 2:
        withdrawal = int(input("Введите сумму снятия кратно 50: "))
        if withdrawal % MULTIPLICITY_REPLENISHMENT == 0:
            commission = 0
            if withdrawal > SUM_LUXURY:
                commission = MAXIMUM_COMMISSION + withdrawal * LUXURY_COMMISSION
            elif MINIMUM_COMMISSION > withdrawal * WITHDRAWAL_FEE:
                commission = MINIMUM_COMMISSION
            elif withdrawal * WITHDRAWAL_FEE > MAXIMUM_COMMISSION:
                commission = MAXIMUM_COMMISSION
            else:
                commission = withdrawal * WITHDRAWAL_FEE

            if sum - withdrawal - commission < 0:
                print("Отказано, недостаточно средств ")
                operation = False
            else:
                sum -= withdrawal - commission
                action += 1
                print(f"Остаток средств {round(sum, 2)} у.е.")
                operation = False
        else:
            operation == 1
            print(f"Остаток средств {round(sum, 2)} у.е.")

    if operation == 3:
        print(f"Остаток на счете {round(sum, 2)} у.е.")
        exit()
