def finish_me(func):
    def wrapped():
        func()
        print('finished')
    return wrapped


@finish_me
def print_something():
    print(f'Start {print_something.__name__} function')


print_something()
