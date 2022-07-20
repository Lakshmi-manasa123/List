
a=[34.6,12,-94.89,'python',0,'c#']
i=0
b=[]
while i<len(a):
    if type(a[i])==int:
        b.append(a[i])
    i=i+1
print(b) 
   