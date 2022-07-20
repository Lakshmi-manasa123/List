
a=['1','2','3','4','5','6','7','8']
i=0
b=[]
while i<len(a):
    c=a[i]+a[i+1]
    b.append(c)
    i+=2
print(b)