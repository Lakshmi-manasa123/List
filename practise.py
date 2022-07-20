# # a=[11,2,45,67,7,33,9,56,77,22]
# # for i in range(len(a)):
# #     for j in range(i+1,len(a)):
# #         if a[i]>a[j]:
# #             a[i],a[j]=a[j],a[i]
# # print(a)


# a=[[1,2,3],[4,5,6],[8,9,10]]
# i=0
# min=a[0]
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i+=1
# print(min)



# a=[101,1010,120,420]
# i=0
# h=[]
# while i<len(a):
#     b=str(a[i])
#     j=0
#     c=" "
#     while j<len(b):
#         if b[j]!="0":
#             c=c+b[j]
#         j=j+1
#     h.append(int(c))
#     i=i+1
# print(h)


# a=[11,222,597,21]
# i=0
# l=[]
# while i<len(a):
#     n=a[i]
#     sum=0
#     while n>0:
#         b=n%10
#         n=n//10
#         sum+=b
#     l.append(sum)    
#     i+=1
# print(l)             


# a=[5,7,32,3,4,1]
# a.remove(5)
# print(a)


# a=["jyo","manasa","hari","giri","gowri"]
# del a[2]
# print(a)


# a=[[78,76,94,86,88],[91,71,98,65,67],[95,45,78,89,92]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum+=a[i][j]
#         j+=1
#     i+=1
# print(sum)



# a=[2,0,0,5,0,7,3,0,4]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(b+c)



# a=[15,17,14,12]
# b=[5,2,3,4]
# i=0
# c=[]
# d=[]
# while i<len(a):
#     c.append((str(a[i])+str(b[i])))
#     d.append((a[i]+b[i]))
#     i+=1
# print(c)
# print(d)


# a=[1,2,3,4,5]
# i=0
# l=0
# b=[]
# while i<len(a):
#     if a[i]>0:
#         l=a[i]
#         h=l**2+1
#         b.append(h)
#     i+=1
# print(b)


# a=[[1,2,3],[4,5,6],[8,9,10]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     min=a[i]
#     while j<len(a[i]):
#         if a[i]>min:
#             b.append(a[i])
#         j+=1
#     i+=1
# print(min)



a=[[1,2,3],[4,5,6],[8,9,10]]
i=0
# min=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        min=a[i][j]
        while j<len(a[i]):
            if a[i][j]<min:
                min=a[i][j]
                # b.append(a[i][j])
            j+=1
        i+=1
    b.append(min)
print(b)

# a=[1,2,[3,4],[5,6]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum+=a[i][j]
#             j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)