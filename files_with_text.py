import os
import random
import string

MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 10
MIN_FILE_SIZE = 1
MAX_FILE_SIZE = 120
NUMBER_ROWS = 10


def create_files_with_extension(num_fal, extension, dir):
    if dir == '':
        os.getcwd()
    else:
        os.chdir(dir)
    for _ in range(num_fal):
        name_length = random.randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length)) + '.' + extension
        for _ in range(NUMBER_ROWS):
            file_size = random.randint(MIN_FILE_SIZE, MAX_FILE_SIZE)
            random_bytes = ''.join(random.choices(string.hexdigits, k=file_size))
            with open(file_name, 'a') as file:
                print(random_bytes, file=file)


if __name__ == '__main__':
    dir = "qwe"
    if not os.path.exists(dir):
        os.mkdir(dir)
    create_files_with_extension(10, 'test', dir)
