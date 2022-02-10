def val_checker(val):
    def _val_checker(func):
        def wrapper(n):
            if val(n) is False:
                raise ValueError(n)
            return func(n)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return print(x ** 3)

try:
    calc_cube(-2)
except ValueError as e:
    print(f"ValueError: wrong val {e}")


# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

