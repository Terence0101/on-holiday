city1,c = input().split(',')
celsius = float(c)

city2,f = input().split(',')
fahrenheit = float(f)

if celsius > ((fahrenheit-32)*(5/9)):
    print(city1)
else:
    print(city2)
