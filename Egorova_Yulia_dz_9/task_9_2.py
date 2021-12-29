class Road:
    def __init__(self,length,width):
        self._length = int(length)
        self._width = int(width)
    def count_mass(self):
        self.mass=self._length*self._width*25*5//1000
        print(f'масса асфальта для вашей дороги равна: {self.mass} т')
a = Road(25,5000)
a.count_mass()