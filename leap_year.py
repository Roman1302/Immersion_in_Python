# Напишите программу, которая запрашивает год и проверяет его на високосность.
print("Программа проверки года на високосность")

year = int(input("Введите год для проверки: "))
# print(a%100, a%400, a%4)

leap_year = 'Это високосный год'
no_leap_year = 'Это не високосный год'

if year % 4 != 0:
    print(no_leap_year)

elif year % 100 == 0:
    if year % 400 == 0:
        print(leap_year)
    else:
        print(no_leap_year)

else:
    print(leap_year)