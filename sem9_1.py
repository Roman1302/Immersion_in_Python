'''Загадование числа с зацикливанием'''


def make(number, num_of_attempts):
    def game():
        attempt = 0
        while attempt < num_of_attempts:
            attempt += 1
            user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
            if user_number < number:
                print('Меньше загадоного')
            elif user_number > number:
                print('Больше загадоного')
            else:
                print(f'Вы отгадали с {attempt} попытки!')
                return True
        else:
            print(
                f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')
            return False

    return game


if __name__ == '__main__':
    number = 10
    num_of_attempts = 5
    res = make(number, num_of_attempts)
    res()
