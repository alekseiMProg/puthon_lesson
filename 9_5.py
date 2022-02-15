class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки!")


class Pen(Stationery):
    def draw(self):
        print(f"Уникальное сообщение: переопределили метод для Pen {self.title}!")


class Pencil(Stationery):
    def draw(self):
        print(f"Уникальное сообщение: переопределили метод для Pencil {self.title}!")


class Handle(Stationery):
    def draw(self):
        print(f"Уникальное сообщение: переопределили метод для Handle {self.title}!")


first = Stationery("Канцелярия")
first.draw()
second = Pen("Ручка")
second.draw()
third = Pencil("Карандаш")
third.draw()
fourth = Handle("Маркер")
fourth.draw()
