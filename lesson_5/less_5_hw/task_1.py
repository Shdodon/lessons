# Напишите функцию, которая принимает на вход строку - абсолютный
# путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


EXP_1 = 'S:\Files\Books\LT\Исходник\Дополнение\War_and_Peace.pdf'
EXP_2 = '"D:\\factor\\glue.txt"'


def split_path(path: str) -> tuple[str, str, str]:
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


print(split_path(EXP_1))
print(split_path(EXP_2))