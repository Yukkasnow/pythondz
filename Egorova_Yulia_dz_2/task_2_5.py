priceies=[52.5,56.7,98.4,45.6,48.00,88.6, 100.2,652.02,40.06,77.77,88.88]
new_prices=[]
for price in priceies:
    cop=price%1
    cop = f"{cop:.2f}".split(".")[-1]
    new_prices.append((f'{price // 1:.0f} руб {cop} коп '))
print(new_prices)
print(sorted(priceies, reverse=True),'max')
print(priceies)
lower_price=sorted(priceies)
print(lower_price,'min')
print(sorted(lower_price[-5:],reverse=True))