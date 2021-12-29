import time
class TrafficLight:

    def running(self):
        self.__color='Красный'
        print(self.__color)
        time.sleep(7)
        self.__color = 'Желтый'
        print(self.__color)
        time.sleep(2)
        self.__color = 'Зеленый'
        print(self.__color)
        time.sleep(5)


t=TrafficLight()

t.running()

