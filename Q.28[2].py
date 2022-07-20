a=[1,1,2,3,4,5,1,2]
b=[]
for i in a:
    if i!=1:
        b.append(i)
print(b)


a=[1,1,2,3,4,5,1,2]
i=0
b=[]
while i<len(a):
    if a[i]!=1:
        b.append(a[i])
    i+=1
print(b)