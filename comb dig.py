a=[0,9,5]
i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
                print(a[i],a[j],a[k])
            k=k+1
        j=j+1
    i=i+1