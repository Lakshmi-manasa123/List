a=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
k=[]
s=[]
i=0 
while i<len(a):
    if type(a[i])==int:
        k.append(a[i])
    else:
        s.append(a[i])
    i=i+1
print(k)
print(s)


