a=[1,2,3,4,5,[6,7,8],[8,2,2]]
b=[]
i=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)
