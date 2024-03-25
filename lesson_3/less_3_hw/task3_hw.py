# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.


backpack_volume = int(input('Enter the volume of the backpack in kg: '))

list_of_equp = {'Консервы,': 3,
                     'Вода,': 4,
                     'Крупа,': 3,
                     'Дождевик,': 0.1,
                     'Розжиг,': 0.2,
                     'Пара носков,': 0.1,
                     'Спички,': 0.01,
                     'Спальный мешок,': 3,
                     'Швейцарский нож,': 0.3,
                     'Кастрюля,': 0.2}


def sort_list(any_set: set):
    global global_list
    if len(any_set) == 1:
        return any_set
    else:
        for item in any_set:
            new_set = any_set.copy()
            new_set.remove(item)
            global_list.add(tuple(sort_list(new_set)))
    return any_set


list_of_equp = dict(sorted(list_of_equp.items(), key=lambda x: x[1]))
global_list = {tuple(list_of_equp)}
sort_list(set(list_of_equp))

print(f'В рюкзак {backpack_volume}кг поместиться:')

for stack in global_list:
    summ_stack = 0
    for item in stack:
        summ_stack += list_of_equp.get(item)
        if summ_stack > backpack_volume:
            break
    else:
        print(*stack, 'весом','=', summ_stack, 'кг')