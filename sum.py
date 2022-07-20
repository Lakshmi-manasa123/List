from re import I


n=int(input("enter teh number"))
sum=0
fact=1
i=1
while i<=n:
    fact=fact*i
    sum=sum+1/fact
    i+=1
print(sum)
