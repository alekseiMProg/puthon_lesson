class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a_1 = (self.a * other.a) + (self.b * other.b * -1)
        b_1 = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(a_1, b_1)

    def __str__(self):
        if self.b >= 0:
            return f"{self.a}+{self.b}j"
        else:
            return f"{self.a}{self.b}j"


comp_1 = ComplexNumber(3, 4)
comp_2 = ComplexNumber(1, 2)
comp_3 = comp_1 + comp_2
comp_4 = comp_1 * comp_2
print(comp_1)
print(comp_2)
print(comp_3)
print(comp_4)

