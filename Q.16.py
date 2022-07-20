
n1=[1,2,3,4,5,6,7,8,9,10]
n2=[2,4,6,8]
i=0
a=[]
b=[]
while (i<len(n1)-1):
    if (i<len(n1)-1):
        a.append(n1[i+1]-n1[i])
    if (i<len(n2)-1):
        b.append(n2[i+1]-n2[i])
    i+=1
print(a)
print(b)