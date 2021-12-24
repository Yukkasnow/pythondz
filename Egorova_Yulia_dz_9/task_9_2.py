class Road:
    def __init__(self,length,width):
        self.length = int(length)
        self.width = int(width)
    def count_mass(self):
        self.mass=self.length*self.width*25*5//1000
        print(f'масса асфальта для вашей дороги равна: {self.mass} т')
a = Road(20,5000)
a.count_mass()