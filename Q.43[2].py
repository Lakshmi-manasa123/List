
list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
k=4
b=[]
i=0
while i<len(list):
    if i==k:
        b.append(20)
        k+=4
    b.append(list[i])
    i+=1
print(b)
