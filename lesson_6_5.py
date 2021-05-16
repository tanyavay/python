#coding:utf-8

#Урок-6 задание-5

class Stationary:
    def __init__(self, title='Может рисовать'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

st = Stationary()
st.draw()

pen = Pen('Parker')
pen.draw()

pencil = Pencil('Koh-I-Nor')
pencil.draw()

handle = Handle('Luxor')
handle.draw()