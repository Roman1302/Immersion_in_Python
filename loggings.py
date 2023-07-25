import logging

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='hw15t01_file_list.txt', filemode='a', format=FORMAT, style='{', level=logging.NOTSET)
general_journal = logging.getLogger()

if __name__ == '__main__':
    print("Not for separate use")
