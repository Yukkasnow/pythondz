class Car:
    def __init__(self,name,color,speed, is_police):
        self.name,self.color,self.speed,=name,color,speed
        self.is_police=is_police
        if self.is_police!='police':
            self.is_police=False
        else:
            self.is_police = True
    def go(self):
        print(f'Мащина {self.color} с водителем {self.name} поехала со скоростью {self.speed} \nПолиция: {self.is_police}')
    def stop(self):
        print(f'Машина {self.color} с водителем {self.name} остановилась')
    def turn(self,direction):
        self.direction=direction
        print(f'Машина {self.color} с водителем {self.name} повернула {self.direction}')
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print('Превышение скорости')
        else:
            print('Не превышает скоростной режим')
class Work_car(Car):
    def show_speed(self):
        if self.speed>40:
            print('Превышение скорости')
        else:
            print('Не превышает скоростной режим')

class Police_car(Car):
    def police(self):
        self.is_police=True
        print('Это полицейская машина')






tc=TownCar('Ivan','red',55, 'med' )
tc.go()
tc.show_speed()
tc.turn('налево')
tc.stop()
wc=Work_car('John','green',45,'police')
wc.go()
wc.show_speed()
wc.turn('направо')
wc.stop()
pc=Police_car('Mike','white',100,'police')
pc.police()
pc.go()
pc.show_speed()
pc.turn('налево')
pc.stop()




