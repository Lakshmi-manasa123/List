
a=[1,1,2,3,4,4,5,1]
b=[]
i=0
while i<len(a):
    c=[]
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        j+=1
    c.append(a[i])
    c.append(count)
    if  c not in b:
        b.append(c)
    i+=1
print(b)        