import json
import os


def deco(func):
    '''
    :param func:
    :return:
    '''

    def wrapper(num, *args, **kwargs):
        filename = f'{func.__name__}.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as fj:
                list_file = json.load(fj)
        else:
            list_file = []
        result = func(num, *args, **kwargs)
        list_file.append({'args': (num, args, kwargs), 'result': result})
        with open(filename, 'w', encoding='utf-8') as fj:
            json.dump(list_file, fj, indent=1)

    return wrapper


@deco
def get_any(num, *args, **kwargs):
    return num


if __name__ == '__main__':
    my_dict = {3: 3, 4: 4}
    get_any(2, 'aa', 'bb', 'cc', my_dict)
