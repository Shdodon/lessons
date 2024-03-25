# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

any_list = [2, 2, 5, 'hello', 6, 5, 'hello']

to_set = set()

for item in any_list:
    if any_list.count(item) > 1:
        to_set.add(item)
print(any_list)
print(list(to_set))