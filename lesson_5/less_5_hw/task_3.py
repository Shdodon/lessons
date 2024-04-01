# Создайте функцию генератор чисел Фибоначчи

number = int(input('How many numbers do you want to generate? '))

def generate_fibonacci_sequence():
     a, b = 0, 1
     while True:
         yield a
         a, b = b, a + b

fibo = iter(generate_fibonacci_sequence())
for _ in range(number):
     print(next(fibo), end=' ')