n=[[8,3,4,],
[1,5,9],
[6,7,2]]
r1=0
r2=0
r3=0
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        if i==0:
            r1=r1+n[i][j]
        elif i==1:
            r2=r2+n[i][j]
        else:
            r3=r3+n[i][j]
        j+=1
    i+=1
# print(r1,r2,r3)
if r1==r2==r3:
    print("row1",r1)
    print("row2",r2)
    print("row3",r3)
else:
    print("not equal",r1,r2,r3)
c1=0
c2=0
c3=0
i=0
while i<len(n):
    j=0
    while j<len(n):
        if i==0:
            c1=c1+n[i][j]
        elif i==1:
            c2=c2+n[i][j]
        else:
            c3=c3+n[i][j]
        j+=1
    i+=1
if c1==c2==c3:
    print("column",c1)
    print("column",c2)
    print("column",c3)
else:
    print("not equal",c1,c2,c3)
d1=0
d2=0
i=0
while i<len(n):
    j=0
    while j<len(n):
        if i==0:
            d1=d1+n[i][j]
        elif i==1:
            d2=d2+n[i][j]
        j+=1
    i+=1
if d1==d2:
    print("diagonal",d1)
    print("diagonal",d2)
else:
    print("not equal",d1,d2)
