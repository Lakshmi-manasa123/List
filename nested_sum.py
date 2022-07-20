# a=[1,2,[3,4],5,6]
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



a=[1,2,3,[4,5,6],[7,8,9],10,[11,12]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)


# a=[2,[3,[6,1],6],3]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                         b.append(a[i][j][k])
#                         k+=1
#             else:
#                 b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)
# i=0
# sum=0
# while i<len(b):
#     if type(b[i])==list:
#         j=0
#         while j<len(b[i]):
#             sum+=b[i][j]
#             j+=1
#     else:
#         sum+=b[i]
#     i+=1
# print(sum)
