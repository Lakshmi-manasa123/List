
a=[1,2,3]
b=[3,2,1]
i=0
p=1
while i<len(a):
    p*=a[i]*b[i]
    i+=1
print(p)   