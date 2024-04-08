# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from string import ascii_lowercase, digits
from random import choices, randint


def create_random_filename(min_length=6, max_length=10):

    return ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_length, max_length)))


def create_files(target_extension, min_size=256, max_size=1024, quantity=5):

    for _ in range(quantity):
        filename = create_random_filename()
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        try:
            with open(f"{filename}.{target_extension}", 'wb') as f:
                f.write(data)
            print(f"Created file: {filename}.{target_extension}")
        except OSError as e:
            print(f"Error creating file: {filename} - {e}")


def rename_files(source_extension, target_extension, slice_range, digit_count=3, new_ending="URNAME"):

    file_list = []
    for dir_path, _, filenames in os.walk(os.getcwd()):
        file_list.extend(filenames)

    for filename in file_list:
        if filename.split('.')[-1] == source_extension:
            try:
                start, end = slice_range
                new_name = f"{filename[start:end]}{new_ending}_{str(0).zfill(digit_count)}.{target_extension}"
                count = 1
                while os.path.exists(new_name):
                    new_name = f"{filename[start:end]}{new_ending}_{str(count).zfill(digit_count)}.{target_extension}"
                    count += 1
                os.replace(filename, new_name)
                print(f"Renamed {filename} to {new_name}")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")



create_files("txt", quantity=2)
create_files("jpeg", quantity=6)
rename_files("jpeg", "md", [4, 2])