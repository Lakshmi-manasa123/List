
# a=[2,4,7,8,66,55]
# i=0
# s=" "
# while i<len(a):
#     if i==0 or i==1:
#         print(a[i],end=",")
#     if i==4 or i==5:
#         s+=str(a[i])
#     i+=1
# print(s)



# a=['gef','is','nice','amazing']
# b=[]
# i=0
# while i<len(a):
#     if i%2==0:
#         b.append(a[i][::-1])
#     else:
#         b.append(a[i])
#     i+=1
# print(b)




# a=['a','b','c','d','e']
# b=['f','g','h','i','j']
# c=[]
# d=b[::-1]
# i=0
# while i<len(a):
#     c.append(a[i]+b[-i-1])
#     i+=1
# print(c)


# a=["manasa","paramatmuni","lakshmi","navgurukul"]
# c=0
# max=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if len(a[i])>max:
#             max=len(a[i])
#             k=a[i]
#         j+=1
#     i+=1
# print(max,k)



a=[1,6,8,0,3,5]
b=int(input("enter a num: "))
# i=0
# # while i<len(a):
# if b not in a:
#     a.append(b)
# else:
#     a.remove(b)
#     # print(b)
#     # i+=1
# print(a)

c=[]
i=0
while i<len(a):
    if b not in a:
        a.append(c[i])
    else:
        a.remove(c)
    i+=1
print(a)