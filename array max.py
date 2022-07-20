a=[1,2,2,3,4,5]
i=0
b=[]
while i<len(a)-1:
    if a[i]<=a[i+1]:
        b.append(a[i+1])
    else:
        b.append(a[i])
    i=i+1
print(b) 
