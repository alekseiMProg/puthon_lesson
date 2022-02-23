class ZeroDivError(Exception):
    pass


try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    if b == 0:
        raise ZeroDivError
except ValueError as e:
    print("Вы ввели не число.")
except ZeroDivError as e:
    print("На ноль делить не-не!")
else:
    print(a / b)
