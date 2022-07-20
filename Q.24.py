a=[1,2,3,1,2,2]
i=0
count=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        count+=1
    i+=1
print(b)
