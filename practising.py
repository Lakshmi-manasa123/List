# a=['flour','cheese','carrot']
# i=0
# while i<len(a):
#     print(i,":",a[i])
#     i+=1


# a=['python','javascript','html']
# i=0
# b=[]
# while i<len(a):
#     s=a[i][-1::-1]
#     b.append(s)
#     i+=1
# print(b)
# print(a)


# a=[10,20,4,6,7,8,9]
# c=0
# for i in a:
#     c+=1
# print(c)


# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# a=[23,456,234,5678,123456]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# a=[123,56,78,937,56,890,54]
# i=0
# max=a[i]
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i+=1
# print(max)


# a=[2,23,56,789,123,345]
# i=0
# min=a[i]
# while i<len(a):
#     if min>a[i]:
#         min=a[i]
#     i+=1
# print(min)


# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# b=[]
# i=0
# while i<len(a):
#     b+=a[i]
#     i+=1
# print(b)



# a=[6,1,3,5,6,3,1]
# i=0
# b=[]
# p=1
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         p*=a[i]
#     i+=1
# print(b)
# print(p)


# n=['manasa','lalasa','navgurukul','paramatmuni']
# a=0
# for i in n:
#     if len(i)>a:
#         a=len(i)
#         n=i
# print(n)




# a=[50,40,23,70,56,12,5,10,7]
# i=0
# fm=0
# sm=0
# tm=0
# while i<len(a):
#     if a[i]>fm:
#         fm=a[i]
#     if a[i]>sm and a[i]!=fm:
#         sm=a[i]
#     if a[i]>tm and a[i]!=sm and a[i]!=fm:
#         tm=a[i]
#     i+=1
# print(fm,sm,tm)


# a="9119"
# i=0
# b=[]
# while i<len(a):
#     b=int(a[i])**2
#     print(b,end="")
#     i+=1

# a=[2,3,4,5]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i+=1
# print(sum)


# a=[[2,3,4,5],[6,7,8]]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a):


# a=[1,2,3,4,5]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1


# a=[1,2,[4,5,[7,6],6,5],7,9]
# i=0

# i=0
# b=[]
# c=[]
# sum1=0
# sum2=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]%2==0:
#             sum1+=a[i]
#             b.append(a[i])
#         else:
#             sum2+=a[i]
#             c.append(a[j])
#         j+=1
#     i+=1
# print(sum1,b)
# print(sum2,c)


# list=[1,2,3,4,5,6,7,8,9,10]
# b=list[7:]
# c=list[2:-7]
# d=list[5:-4]
# print(c+d+b)



# b=[2,3,[4,5,7,[7,2,[3],4,7],2,3],5]
# print(b[2][3])

# a=[5,6,[2,3,[4,5],6,7,8],8]
# print(a[2][3])

# a=[[5,6,7,[5,6],8],9,7,[5,6]]
# print(a[0][3][1])
# print(a[1])
# print(a[3][1])

# a=[[[3,2],7,8,[2,4],5],8,7]
# # print(a[0][2])
# # print(a[0][4])
# # print(a[2])
# print(a[0][1])
# print(a[0][4])
# print(a[0][2])

# a=[[[[2,4,[3,[8]]]]]]
# # print(a[0][0][0][0])
# # print(a[0][0][0][1])
# print(a[0][0][0][0])
# print(a[0][0][0][1])
# print(a[0][0][0][2][0])
# print(a[0][0][0][2][1][0])


# a="my name is jyothsna"
# b=print(a[11:])
# d=print(a[-9:])
# print(b+d)

# a=[2,4,6,1,0,2,5,1]
# b=print(a[4:-3])
# print(b)

# a="27may2022"
# # b=print(a[-1::-1])
# b=a[:-7]
# c=a[5:]
# d=a[2:-4]
# print(c+d+b)

# a="27may2022"
# b=a[2:]
# c=a[:-7]
# # d=a[-4:5]
# # print(b+c)

# a=[1,2,3,4,5,6]
# a.pop(4)
# print(a)

# a=[1,2,3,4,5,6,7,8]
# a.remove(8)
# print(a)


# a=[1,2,3,4,5,6,7,8]
# del a[5]
# print(a)

# a=[1,2,3,4,5,]
# a.append(5)
# print(a)


# a=[1,2,3,4,5]
# a.clear()
# print(a)

# a=[1,2,3,4,5]
# a.copy()
# print(a)

# a=[1,2,3,4,5,6]
# a.count(0)               count is a variable
# print(a)


# a=[1,2,3,4,5]
# a.extend([2,3,4,5,6])
# print(a)


# a=[1,2,3,4,5]
# a.index(5)           used for sample list
# print(a)


# a=[1,2,3,4,5]
# a.reverse()        #reverses for nested list as it is but come in front
# print(a)


# a=[2,4,7,9,4]
# a.sort()
# a.reverse()
# a.extend([4,5,67,7,8,9,10])
# a.remove(7)
# a.append(1)
# print(a)


# a="123456"
# i=0
# while i<len(a):
#     j=len(a)-(i+1)
#     b=int(a[i])*10**j
#     print(b)
#     i+=1


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


# a=[2,3,1,9,6,5]
# i=0
# max=0
# b=[]
# while i<len(a):#     if a[i]>max:
#         max=a[i]
#     b.append(max)
#     i+=1
# print(b)


# a=[1,2,3,4]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     if a[i]>sum:
#         sum=a[i]
#     b.append(sum)
#     i+=1
# print(b)


# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a)-1:
#     c=[a[i],a[i+1]]
#     b.append(c)
#     i=i+1
# print(b)


# a=[2,3,7,8,66,55]
# b=a[:-4]
# c=a[4:]
# d=str(b+c)
# print(d)


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



# a=["n","i","t","i","n"]
# b=a[-1::-1]
# if b==a:
#     print("palindrome")
# else:
#     print("not a palindrome")


# a=[10,20,30,40]
# b=[100,200,300,400]
# c=b[::-1]
# i=0
# while i<len(a):
#     print(a[i],c[i])
#     i+=1

# a=['a','b','c','d','e']
# b=['f','g','h','i','j']
# c=[]
# d=b[::-1]
# i=0
# while i<len(a):
#     c.append(a[i]+b[-i-1])
#     i+=1
# print(c)


# a=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(b)
# print(c)


a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        b.append(a[i][j])
        sum+=a[i][j]
        j+=1
    i+=1
    print(sum,end=" ")