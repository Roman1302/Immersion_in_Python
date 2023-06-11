'''Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.'''
import string

a = str(input("Введите текст: "))

text_low = a.lower()

text_clear = text_low.translate(str.maketrans('', '', string.punctuation))
# print(f'\n{text_clear}')
text_list = text_clear.split(' ', )

text_sor = sorted(text_list)
# print(text_sor)
# print(text_sor[0], len(text_sor))

sp_sum = [len(i) for i in text_sor]
# print(sp_sum)

max_value = max(sp_sum)
# print(max_value)
i = 0
while i < len(text_sor):
    print(f'{i + 1:<2} {text_sor[i]:>{max_value}}')
    i += 1
