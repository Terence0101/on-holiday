beef = int(input())
pork = int(input())
lamb = int(input())

if beef >= 10:
    pork = pork + (beef//10)
else:
    pork = pork
    
if pork >= 5:
    lamb = lamb + (pork//5)
else:
    lamb = lamb

print ('beef\tpork\tlamb\n',beef,'\t',pork,'\t',lamb,sep="")
