
num=int(input("enter a num"))
sum=0
temp=num
while num>0:
    i=1
    f=1
    rem=num%10
    while i<=rem:
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if sum==temp:
    print("strong num")
else:
    print("not a strong num")