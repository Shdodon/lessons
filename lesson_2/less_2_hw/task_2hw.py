import fractions

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
a = fractions.Fraction(input('Enter a: '))
print(a)
b = fractions.Fraction(input('Enter b: '))
print(b)
sum = a + b
mult = a * b
print(f'{a} + {b} = {sum}\n{a} * {b} = {mult}')