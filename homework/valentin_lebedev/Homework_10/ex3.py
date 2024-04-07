
def regulation(func):
    def wrapped(a, b):
        if a == b:
            return func(a, b, '+')
        elif a > b:
            return func(a, b, '-')
        elif a < b:
            return func(a, b, '/')
        elif a < 0 or b < 0:
            return func(a, b, '*')
    return wrapped


@regulation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(3, 5))
