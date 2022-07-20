#a=[1,1,2,3,4,4]
# i=0
# b=[]
# # count=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     elif a[i]!=1:
#         print(a[i])
#     elif a[i]!=4:
#         print(a[i])
#         # count+=1
#     i+=1
# print(b)
# # print(count)



a=[[1,2,3],4,[5,6,7],8,[9,10,11],12]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==list:
                        b.append(a[i][j][k])
                    else: #type(a[i])!=list:
                        b.append(a[i][j][k])
                    k+=1
                b.append(a[i][j])
            else: #type(a[i][j])!=list:
                b.append(a[i][j])
            j+=1
        b.append(a[i])
    else:#type(a[i][j][k])!=list:
        b.append(a[i])
    i+=1
print(b)
