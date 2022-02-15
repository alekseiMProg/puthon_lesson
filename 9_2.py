class Road:
    WEIGHT = 25

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def all_weight(self, t):
        print((self._length * self._width * Road.WEIGHT * t) // 1000)


one = Road(20, 5000)
one.all_weight(5)
