#coding:utf-8

#Урок-6 задание-4

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости" if self.speed > 60 else "Скорость не превышена"}')

class WorkCar(Car):
    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости" if self.speed > 40 else "Скорость не превышена"}')

class SportCar(Car):
    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar('Bus', 'yellow', 50)
town_car.turn(0)
town_car.show_speed()

work_car = WorkCar('Truck', 'blue', 80)
work_car.go()
work_car.show_speed()

sport_car = SportCar('Ferrari', 'red', 280)
sport_car.show_speed()

police_car = PoliceCar('Police', 'white', 100)
police_car.stop()
police_car.show_speed()
print(police_car.is_police)