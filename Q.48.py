
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=0
b=[]
k=0
while (i<len(a)):
    j=0
    c=[]
    while j<3 and k!=len(a):
        c.append(a[k])
        j+=1
        k+=1
    b.append(c)
    if k==len(a):
        break
    i+=1
print(b)
