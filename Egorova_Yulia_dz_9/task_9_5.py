class Stationery:
    title='Parent'
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Тескт записан')
class  Pencil(Stationery):
    def draw(self):
        print('Картинка нарисована')
class Handle(Stationery):
    def draw(self):
        print('Текст выделен')
s=Stationery()
s.draw()
p=Pen()
p.draw()
pp=Pencil()
pp.draw()
h=Handle()
h.draw()
