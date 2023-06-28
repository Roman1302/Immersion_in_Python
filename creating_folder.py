import os

'''создание папки'''


def dir(folder_name):
    if folder_name == '':
        folder_name = os.getcwd()
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


if __name__ == '__main__':
    dire = ''
    dir(dire)
