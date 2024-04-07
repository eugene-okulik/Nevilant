def repeat_me(func):
    def wrapped(*args):
        for _ in range(*args):
            func()
    return wrapped


@repeat_me
def print_something1():
    print(f'Start {print_something1.__name__} function')


print_something1(2)


def repeat_me(count):
    def decorator(func):
        def wrapped():
            for _ in range(count):
                func()
        return wrapped
    return decorator


@repeat_me(count=3)
def print_something2():
    print(f'Start decorator with arguments function')


print_something2()
