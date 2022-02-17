class Cell:
    def __init__(self, el):
        self.el = el

    def __str__(self):
        return f"{self.el}"

    def __add__(self, other):
        return Cell(self.el + other.el)

    def __sub__(self, other):
        if self.el - other.el > 0:
            return Cell(self.el - other.el)
        else:
            return "Error. Subtracting values less than zero."

    def __mul__(self, other):
        return Cell(self.el * other.el)

    def __floordiv__(self, other):
        return Cell(self.el // other.el)

    def make_order(self, n):
        _m = self.el
        my_list = []
        while _m > 0:
            if _m > n:
                my_list.append(f"{'*' * n}\n")
                _m -= n
            else:
                my_list.append(f"{'*' * _m}")
                _m -= n
        return "".join(my_list)


a = Cell(2)
b = Cell(10)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(b.make_order(3))
