a=[1,2,3,-1,0,-2,0,-3,0,0]
##o/p=[1,2,3,0,0,0,0,-1,-2,-5]
##o/p=[1,3,5,-1,-2,-5,0,0,0,0]
i=0
b=[]
c=[]
d=[]
while i<len(a):
    if a[i]>0:
        b.append(a[i])
    elif a[i]<0:
        c.append(a[i])
    elif a[i]==0:
        d.append(a[i])
    i+=1
print(b+c+d)
print(b+d+c)

# a.sort()
# print(a)