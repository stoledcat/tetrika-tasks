def strict(func):
    def wrapper(*args):
        for arg in args:
            if (
                not isinstance(arg, int)
                or isinstance(arg, bool)
                or isinstance(arg, str)
            ):
                raise TypeError("Неправильные аргументы")
        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
