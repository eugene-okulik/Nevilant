import random
import sys

# Задание 1

salary = int(input("Введите сумму: "))
bonus = random.choice([True, False])

if bonus:
    print(f'{salary}, {bonus} - ${salary + random.randint(1, 10000)}')
else:
    print(f'{salary}, {bonus} - ${salary}')

# Задание 2

sys.set_int_max_str_digits(1000000)


def fib(limit):
    a = 0
    b = 1
    for i in range(limit):
        yield a
        a = b
        b = a + b


def fib_index(index):
    for i, number in enumerate(fib(index + 1)):
        if i == index:
            return number


print(fib_index(4))
print(fib_index(199))
print(fib_index(999))
print(fib_index(99999))
