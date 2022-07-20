a=[4,6,4,3,3,4,3,4,3,8]
# a=[5,4,6,7,5,4,3,2,5,4,9]
k=4
i=0
count=0
while i<len(a):
    if a[i]==k:
        count+=1
    i+=1
print(count,k)