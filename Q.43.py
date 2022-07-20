
a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
k=3
b=[]
i=0
while i<len(a):
    if i==k:
        b.append('Z')
        k+=3
    b.append(a[i])
    i+=1
print(b) 