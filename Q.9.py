a=[50,40,23,70,56,12,5,10,7]
fm=0
sm=0
tm=0
i=0
while i<len(a):
    if a[i]>fm:
        fm=a[i]
    if a[i]>sm and a[i]!=fm:
        sm=a[i]
    i+=1
i=0
while i<len(a):
    if a[i]>tm and a[i]!=fm and a[i]!=sm:
        tm=a[i]
    i+=1
print(fm,sm,tm)