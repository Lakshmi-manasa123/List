a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i<len(a):
    sum=0
    j=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j+=1
    b.append(sum)
    i+=1
print(b)
