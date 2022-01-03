from abc import ABC, abstractmethod
class Clothes:
    def __init__(self, par):
        self.par=par
    @abstractmethod
    def consumption(self):
        pass

class Suit(Clothes):
    @property
    def consumption(self):
        return f'потребуется {2*self.par+0.3} ткани для пошива костюма'

class Coat(Clothes):
    @property
    def consumption(self):
        return f'потребуется {self.par/6.5+0.5} ткани для пошива пальто'



c=Coat(50)
s=Suit(160)
print(s.consumption)
print((c.consumption))
