'''Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''

print("Программа определения простого и составного числа")
logic = True

while logic:
    try:
        number = int(input("Введите целое число от 1 до 100 000: "))

        if number < 1 or number > 99999:
            logic = True
            print("ОШИБКА! Число должно быть в диапазоне от 1 до 100 000.")

        elif number == 1 or number == 2:
            logic = False
            print("Число", number, "- является простым")

        elif number < 6:
            for i in range(2, int(number)):
                if number % i == 0:
                    text = "- является составным"
                    break
                else:
                    text = "- является простым"
            print("Число", number, text)
            logic = False

        else:
            for i in range(2, int(number/2)):
                if number % i == 0:
                    text = "- является составным"
                    break
                else:
                    text = "- является простым"
            print("Число", number, text)
            logic = False

    except ValueError:
        logic = True
        print("ОШИБКА!")