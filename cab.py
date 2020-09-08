km = float (input())
price = 70

if km >= 1.25:
    price = 70 + ((km-1.25)/0.25*5)
else:
    prince = price
    
print('Mr. White needs to pay',round(price),'dollars.')
