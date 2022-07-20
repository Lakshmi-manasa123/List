
a=["python","javascript","HTML","graphic design"]
i=0
b=[]
while i<len(a):
    s=a[i][-1::-1]
    b.append(s)
    i+=1
print(b)
i=0
while i<len(b):
    c=b[-1::-1]
    i+=1
print(c)