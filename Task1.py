# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
from functools import wraps


def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if args != ():
            if kwargs != {}:
                print(f'{func.__name__} called with {str(args)[1:-1]}; {str(kwargs)[1:-1]}')
            else:
                print(f'{func.__name__} called with {str(args)[1:-1]}')
        elif kwargs != {}:
            print(f'{func.__name__} called with {str(kwargs)[1:-1]}')
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


@logger
def foo(*args, **kwargs):
    return None


add(1, 2)
square_all(1, 2, 3, 4, 5)
foo(1, 2, 3, 4, name='Mihail', surname='Barkov')
foo(name='Mihail', surname='Barkov')
