# a=[2,[3,[6,1],6],3]
# i=0
# b=[]
# y=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         d=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 l=0
#                 while k<len(a[i][j]):
#                     if type(a[i][j][k])==int:
#                         l+=a[i][j][k]
#                     k+=1 
#                 b.append(l) 
#             else:
#                 d+=a[i][j]
#             j+=1
#         b.append(d)
#     else:
#         y=y+(a[i])
#     i+=1
# 

a=[1,2,3]
i=0
k=[]
while i<len(a):
    j=i
    b=[]
    while j<len(a):
        b.append(a[j])
        print(b,end="")
        j=j+1
    i=i+1
print()

