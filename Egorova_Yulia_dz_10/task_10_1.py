class Matrix:
    i=0
    def __init__(self, my_list):
        self.my_list=my_list

    def __str__(self):
        i=0
        while i!=len(self.my_list):
             print(self.my_list[i])
             i+=1
        print('-----------------------------------------------------------------------')
        return ''


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)







a=Matrix([[2,3,4],[5,6,7]])
b=Matrix([[8,9,10],[11,12,13]])
a.__str__()
b.__str__()
print(a.__add__(b))