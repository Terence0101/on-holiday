fullname = str(input ())
price = int(input())

addtax = round(price*1.1)

pay = 0
if addtax >= 200:
    pay = addtax-((addtax//200)*10)
else:
    pay = addtax

print (fullname.split()[1],"needs to pay",pay,"dollars")
