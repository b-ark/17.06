# Write a decorator `arg_rules` that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrap(*args):
            check = ''.join(args)
            for a in args:
                if not isinstance(a, type_):
                    raise TypeError(f'Переменная должна иметь тип {type_}')
            if len(check) > max_length:
                raise ValueError(f'Выражение не должно содержать больше {max_length} символa(ов)')
            for symbols in contains:
                if symbols not in check:
                    raise NameError(f'Выражение должно содержать {contains}')
            slogan = func(check)
            return slogan
        return wrap
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


try:
    print(create_slogan('S@SH05'))  # 'S@SH05 drinks pepsi in his brand new BMW!'
    print(create_slogan('johndoe05@gmail.com'))  # is False
except TypeError as massage:
    print(massage)
except ValueError as massage:
    print(massage)
except NameError as massage:
    print(massage)
