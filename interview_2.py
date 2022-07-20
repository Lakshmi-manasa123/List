# a=[30300,20100,60100,22000,179900]
# b=[]
# i=0
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i=i+1
# print(b)



# a=[1,3,7,2,9,11]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2!=0:
#         b.append(a[i])
#     i+=1
# print(b)


# a=[[3,7,8],[7,9,7],7,8,2]    
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if type (a[i])==list:
#         b.extend(a[i])
#     else:
#         b.append(a[i])
#     i+=1
# print(b)
# i=0
# sum=0
# while i<len(b):
#     sum+=b[i]
#     i+=1
# print(sum)    

                    # 0 1 2  0 1 2  
a=[2,3,4,[2,3],7,8,[5,6,7,[5,7,9],7,2]]
#    0,1,2, 0   ,3,4, 1        2    5 6
print(a[5])
