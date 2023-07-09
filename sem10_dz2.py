'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''
from fractions import Fraction


class Conclusion:
    def __init__(self, drob):
        self.drob1 = drob

    def translate_str_to_digit(self, str_drob):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_translation(self, data):
        a_ch = self.translate_str_to_digit(data)[0]
        a_zn = self.translate_str_to_digit(data)[1]
        list_r = []
        divider = 0

        for i in range(2, int(a_ch + 1)):
            if a_ch % i == 0 and a_zn % i == 0:
                divider = i
        if a_ch == 0:
            list_r = ["0"]
        elif divider > 0:
            # print(3)
            a_ch1 = a_ch / divider
            a_zn1 = a_zn / divider
            if a_ch1 > a_zn1:
                divider = a_ch1 // a_zn1
                a_ch = a_ch1 % a_zn1
                list_r = [str(int(divider)), str(int(a_ch)), str(int(a_zn1))]
            if a_ch == a_ch1 * divider:
                list_r = [str(int(a_ch1)), str(int(a_zn1))]
            if a_zn1 == 1:
                list_r = [str(int(a_ch1))]
        elif a_ch > a_zn:
            # print(1)
            divider = a_ch // a_zn
            a_ch = a_ch % a_zn
            list_r = [str(int(divider)), str(int(a_ch)), str(int(a_zn))]
        else:
            # print(2)
            list_r = [str(int(a_ch)), str(int(a_zn))]

        # print(888, list_r)
        return list_r

    def __str__(self):
        # print(125, str(self.data_translation(self.drob1)[0]))
        if len(self.data_translation(self.drob1)) == 3:
            return f'{self.data_translation(self.drob1)[0] + "+" + self.data_translation(self.drob1)[1] + "/" + self.data_translation(self.drob1)[2]}'
        elif len(self.data_translation(self.drob1)) == 2:
            return f'{self.data_translation(self.drob1)[0]}/{self.data_translation(self.drob1)[1]}'
        else:
            return f'{self.data_translation(self.drob1)[0]}'


class Sum:

    def __init__(self, drob1, drob2):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_sum(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        ch = a_ch * b_zn + b_ch * a_zn
        zn = b_zn * a_zn
        res = str(ch) + "/" + str(zn)
        # print("res", res)
        return res

    def __str__(self):
        # print(100, Conclusion(self.data_sum(self.drob1, self.drob2)))
        return f'{self.drob1} + {self.drob2} = {Conclusion(self.data_sum(self.drob1, self.drob2))}'


class Multy:

    def __init__(self, drob11, drob22):
        self.drob11 = drob11
        self.drob22 = drob22

    def translate_str_to_digit(self, str_drob):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_mult(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        res = str(int(a_ch * b_ch)) + "/" + str(int(a_zn * b_zn))
        # print(666, res)
        return res

    def __str__(self):
        # print(222, self.data_mult(self.drob11, self.drob22))
        return f'{self.drob11} * {self.drob22} = {Conclusion(self.data_mult(self.drob11, self.drob22))}'


if __name__ == '__main__':
    a = '9/4'
    b = '5/2'

    # aaa=Conclusion(a)
    # print("aaa", aaa)

    sum1 = Sum(a, b)
    mult1 = Multy(a, b)
    print(sum1)
    print(mult1)
    print(f'\nПроверка с помощью fractions:')
    print(f"{a} + {b} = {Fraction(a) + Fraction(b)}")
    print(f"{a} * {b} = {Fraction(a) * Fraction(b)}")
