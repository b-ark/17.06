# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
from functools import wraps


def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrap(*args):
            decorated_slogan = func(''.join(args))
            for word in words:
                decorated_slogan = decorated_slogan.replace(str(word), '*')
            return decorated_slogan
        return wrap
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Mihail'))
