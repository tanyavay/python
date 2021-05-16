#coding:utf-8

#Урок-6 задание-3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

w = Position('Иван', 'Иванов', 'вахтер', 10300, 500)
print(w.get_full_name())
print(w.get_total_income())