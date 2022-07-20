a=input("enter any num")
i=0
s=0
while i<len(str(a)):
    s=s+int(a[-(i+1)])*2**i
    i+=1
print(s)



