
a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        b.append(a[i][j])
        sum+=a[i][j]
        j+=1
    i+=1
    print(sum,end=" ")
    
