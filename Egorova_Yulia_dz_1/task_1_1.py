duration=95550

if duration<60:
    print(f'{duration} сек')
if 60<duration<=3600:
    min=duration//60
    sec=duration%60
    print(f'{min} мин {sec} сек')
if 3600<duration<=86400:
    hour=duration//3600
    min=duration%3600//60
    sec=duration%60
    print(f'{hour} ч {min} мин  {sec} сек')
if duration>86400:
    dd=duration//86400
    hour=duration%86400//3600
    min=duration%3600//60
    sec=duration%60
    print(dd, hour, min, sec)


