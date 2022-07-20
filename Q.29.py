
a=[5,6,[],3,[],[],9]
# b=len(a)
b=[]
i=0
while i<len(a):
    if a[i]!=[]:
        # print(a[i])
        b.append(a[i])
    i+=1
print(b)
