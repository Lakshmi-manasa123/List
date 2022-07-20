a=[1,2,3,[4,[5,6,[7,8,[9,10],11],12],13],14]
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
                        l=0
                        while l<len(a[i][j][k]):
                            if type(a[i][j][k][l])==list:
                                m=0
                                while m<len(a[i][j][k][l]):
                                        b.append(a[i][j][k][l][m])
                                        sum+=a[i][j][k][l][m]
                                        m+=1
                            else:
                                b.append(a[i][j][k][l])
                                sum+=a[i][j][k][l]
                            l+=1
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
