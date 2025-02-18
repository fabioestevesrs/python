def to_upper(function):
    def wrapper():
        return function().upper()

    return wrapper


def split_name(function):
    def wrapper():
        return function().split()

    return wrapper
