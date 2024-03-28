'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def my_function(**kwargs) -> dict[str, str]:
    return {str(value): key for key, value in kwargs.items()}


result = my_function(a=1, b='fff', c=[1, 2, 3])
print(result)