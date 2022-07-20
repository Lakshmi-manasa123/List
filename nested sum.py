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



# a=[[4,2,6],[5,4,2],[1,2,3]]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     print(sum)
#     i+=1



# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# list=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     # print(sum)
#     list.append(sum)
#     i=i+1
# print(list) 


a=[[[[[2,3,[4,3],9]]]]]
print(a[0][0][0][0][1])