a=[4,[7,5,[4,0,7],5,[0],4],5]
i=0
b=[]
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==list:
                        b.append(a[i][j][k])
                    else:
                        b.append(a[i][j][k])
                        sum+=a[i][j][k]
                    k+=1
            else:
                b.append(a[i][j])
                sum+=a[i][j]
            j+=1
    else:
        b.append(a[i])
        sum+=a[i]
    i+=1
print(b)
print(sum)

# print(a[1][2][2])