import sys
if __name__=='__main__':
    period = list(map(int, sys.argv[1:]))
    with open('bakery.csv') as f:
        text = f.readlines()
        if len(period == 2):
            for line in text[period[0] - 1:period[1]]:
                print(line.strip())
        elif len(period == 1):
            for line in text[period[0] - 1]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()


