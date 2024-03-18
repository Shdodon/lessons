"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 0
MAX_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

while count < MAX_COUNT:
    user_num = int(input("Ваше число: "))
    count += 1

    if user_num == num:
        print("Вы угадали число!")
        break

    elif user_num > num:
        print("Загаданное число больше!")

    elif user_num < num:
        print("Загаданное число меньше")
else:
    print("Увы! Попытки исчерпаны!")