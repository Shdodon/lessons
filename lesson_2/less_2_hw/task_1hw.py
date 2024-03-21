"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
HEX = 16

num = int(input('Enter number: '))
temp = num
hex_digits = '0123456789abcdef'
hex_num = ''

while num > 0:
    remainder = num % HEX
    hex_digit = hex_digits[remainder]
    hex_num = hex_digit + hex_num
    num //= HEX
print("Шестнадцатеричное число:", hex_num)


check_hex = hex(temp)
print(check_hex)