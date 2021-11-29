percents=range(0,101)
for percent in percents:
    if percent==1 or percent%10==1:
        print(percent, 'процент')
    if 2<=percent<=4:
        print(percent, 'процента')
    if 11<=percent<=14:
        print(percent, 'процентов')
    if 2<=percent%10<=4 and percent>14:
        print(percent, 'процента')
    if 5<=percent%10<=9 or percent%10==0:
        print(percent, 'процентов')
