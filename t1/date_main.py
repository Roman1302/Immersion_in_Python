from t1.date_verification_module import date_check


def start(ff):
    print(date_check(ff))


if __name__ == '__main__':
    f = input("Введите дату: ")
    start(f)
