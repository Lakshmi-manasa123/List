# x="nitin"
# y=x[::-1]
# for i in x:
#     # y=i+y
#     if y==x:
#         print("yes",y,"is palindrome")
#     else:
#         print("not",y,"is not a palindrome")




a=input("enter:")
i=0
l=int(len(a))
while i<int(l/2+1):
    if a[i]==a[-i-1]:
        i+=1
    else:
        break
if (i<l/2):
    print("not")
else:
    print("yes")

