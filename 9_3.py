class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self.wage = w
        self.bonus = b
        self._income = {'Оклад': w, 'Премия': b}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя Фамилия: {self.name, self.surname}")

    def get_total_income(self):
        print(f"Оклад + премия: {self._income['Оклад'] + self._income['Премия']}")


manager = Position("Илья", "Иванов", "Менеджер", 7000, 1000)
manager.get_full_name()
manager.get_total_income()
