from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def __init__(self, title):
        self.title = title


class Coat(Cloth):
    def __init__(self, title, v):
        super().__init__(title)
        self.v = v

    @property
    def fabric(self):
        if isinstance(self.v, int) or isinstance(self.v, float):
            return self.v / 6.5 * 0.5
        else:
            return f"{self.v} must be a number"


class Costume(Cloth):
    def __init__(self, title, h):
        super().__init__(title)
        self.h = h

    @property
    def fabric(self):
        if isinstance(self.h, int) or isinstance(self.h, float):
            return 2 * self.h + 0.3
        else:
            return f"{self.h} must be a number"


def total_fabric(*args):
    pass


a = Costume("black", 5)
print(a.fabric)
b = Coat("yellow", 13)
print(b.fabric)
print(a.fabric + b.fabric)