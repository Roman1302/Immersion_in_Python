COUNT = 3


def param(count):
    '''
    :param count:
    :return:
    '''

    def deco(func):
        res_list = []

        def wrapper(*args):
            for _ in range(count):
                res = func(*args)
                res_list.append(res)
            print(res_list)

        return wrapper

    return deco


@param(COUNT)
def my_func(*args):
    return (args)


if __name__ == '__main__':
    my_func('Hello world')
    my_func('world 156')
