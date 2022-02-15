class Car:

    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed}")

    def go(self):
        print(f"Автомобиль {self.name} цвета {self.color} начал движение!")

    def stop(self):
        print(f"Автомобиль {self.name} цвета {self.color} остановился!")

    def turn(self, direction):
        print(f"Автомобиль {self.name} цвета {self.color} изменил направление: движется {direction}!")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Вы привышаете установленную законом скорость. Ваша скорость равна: {self.speed}.")
        else: super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Вы привышаете установленную законом скорость. Ваша скорость равна: {self.speed}.")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


one = Car(40, "black", "Mazda", False)
one.go()
one. turn("вправо")
one.stop()

two = TownCar(50, "red", "Toyota", False)
two.show_speed()
two.speed = 80
two.show_speed()

