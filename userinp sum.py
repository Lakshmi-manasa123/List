l=[]
n=int(input("enter a num"))
i=1
while i<=n:
    i+=1
    e=int(input("enter a num"))
    l.append(e)
print(l)
i=0
sum=0
while i<len(l):
    sum+=l[i]
    i+=1
print(sum)