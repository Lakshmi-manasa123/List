a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
min=1
n=[]
k=[]
while i<len(a):
    if max<len(a[i]):
        max=len(a[i])
        n=a[i]
    if min>=len(a[i]):
        min=len(a[i])
        k=a[i]
    i+=1
print(max,n)
print(min,k)
