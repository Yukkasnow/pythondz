names=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i=0
for name in names:
    name = str(names[i])
    name = name.split()
    print(f'Привет, {name[-1].title()}')
    i+=1