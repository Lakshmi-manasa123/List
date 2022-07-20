# numbers=[50,40,23,70,56,12,5,10,7]
# print(max(numbers))


# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print(numbers[-2])

# a=["delhi","gujarat","rajasthan","punjab","kerala"]
# a.reverse()
# print(a)


# a=["to get a job","to buy a house","to buy a car","to settle in a highest position","study hard"]
# for i in a:
#     print(i)

# a=["oil","sugar","maggi","mustard seeds","ground nuts","shampoos","soaps"]
# for i in a:
#     print(i)


# a=["oil","sugar","maggi","mustard seeds","ground nuts","shampoos","soaps","salt"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=[40,70,60,20,50]
# l=len(a)
# for i in range(l):
#     print(a[i])

# a=[40,70,60,20,50]
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i=i+1


# a=["wake up early in the morning","brushing after wake up","praying to god","respecting parents"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=["wake up early in the morning","brushing after wake up","praying to god","respecting parents"]
# [print(i) for i in a]

# a=["python","javascript","HTML","graphic design"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=[50,40,23,70,56,12,5,10,7]
# i=0
# for j in a:
#     i+=1
# print(i)


# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# c=0
# while i<len(numbers):
#     a=numbers[i]
#     if a>=20 and a<=40:
#         c+=1
#     i+=1
# print(c)

# a=["n","i","t","i","n"]
# a=["m","a","n","a","s","a"]
# b=a[-1::-1]
# if b==a:
#     print("palindrome")
# else:
#     print("not a palindrome")


# a=[1,0,0,1,1,0,1,1]
# i=0
# s=0
# while i<len(a):
#     s=s+a[-(i+1)]*2**i
#     i=i+1
# print(s)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)


# l1=[10,20,30,40]
# l2=[100,200,300,400]
# b=l2[::-1]
# i=0
# while i<len(l1):
#     print(l1[i],b[i])
#     i=i+1


# A=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# k=[]
# s=[]
# i=0 
# while i<len(A):
#     if type(A[i])==int:
#         k.append(A[i])
#     else:
#         s.append(A[i])
#     i=i+1
# print(k)
# print(s)


# a=[1,2,2,3,4,5]
# i=0
# b=[]
# while i<len(a)-1:
#     if a[i]<=a[i+1]:
#         b.append(a[i+1])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b) 


# a=[0,9,5]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1


# a=[1,2,[3,2,[5,6],3,[4]],89,80]
# b=[] 
# i=0 
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])==list:
#                 k=0 
#                 while k<len(a[i][j]): 
#                     b.append(a[i][j][k]) 
#                     k+=1 
#             else: 
#                 b.append(a[i][j])
#             j=j+1 
#     else:
#         b.append(a[i]) 
#     i=i+1 
# s=0 
# l=0 
# while l<len(b):
#     s+=b[l] 
#     l+=1 
# print(s)



# l1=[1,2,3,4,5,6]
# l2=[2,3,1,0,6,7]
# i=0
# while i<len(l1):
#     if l1[i] not in l2:
#         print(l1[i])
#     i+=1


# a=[1,2,3,4,5,6]
# b=[2,3,1,0,6,7]
# for i in a:
#     if i not in b:
#         print(i)



# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# b=0
# while i<3:
#     s=marks[0][b]+marks[1][b]+marks[2][b]
#     i+=1
#     b+=1
#     print(s)


# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# b=0
# for i in range(5):
#     s=marks[0][b]+marks[1][b]+marks[2][b]
#     b+=1
#     print(s)


# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# b=0
# s1=0
# s2=0
# s3=0
# while i<5:
#     s1= a[0][b]+s1
#     s2=a[1][b]+s2
#     s3=a[2][b]+s3
#     i+=1
#     b+=1
# print(s1/5)
# print(s2/5)
# print(s3/5)
# print("total marks for 3 years is :",s1+s2+s3)

# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len([a[i]]):
#         s+=a[i][j]
#         j+=1
#     i+=1
# print(s)


# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len([a[i]]):
#         s+=a[i][j]
#         j+=1
#     i+=1
# print(s)


# a=30
# n=[10,11,12,13,16,17,18,19]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if n[i]+n[j]==a:
#             print([n[i],n[j]])
#         j+=1
#     i+=1



# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num:",a[i])
#     else:
#         print("odd num:",a[i])
#     i=i+1

# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num:",a[i])
#         sum_even=sum_even+a[i]
#     else:
#         print("odd num:",a[i])
#         sum_odd=sum_odd+a[i]
#     i=i+1
# print("even sum",sum_even)
# print("odd sum",sum_odd)


# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# ec=0
# oc=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         sum_even=sum_even+a[i]
#         ec+=1
#     else:
#         sum_odd=sum_odd+a[i]
#         oc+=1
#     i=i+1
# print("even avg",sum_even/ec)
# print("odd avg",sum_odd/oc)
# print("total marks for 3 years is:",sum_even+sum_odd


# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# avg_even=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num",a[i])
#         sum_even=sum_even+a[i]
#     else:
#         print("odd num",a[i])
#         sum_odd=sum_odd+a[i]
#         i=i+1
#     print(sum_even)
#     avg_even=sum_even/b
#     print(avg_even)
#     print(sum_odd)
#     avg_odd=sum_odd/b
    # print(avg_odd/b)



# a=[1,1,2,3,4,4,5,1]
# b=[]
# i=0
# while i<len(a):
#     c=[]
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     c.append(a[i])
#     c.append(count)
#     if  c not in b:
#         b.append(c)
#     i+=1
# print(b)        
    




# n1=[1,2,3,4,5,6,7,8,9,10]
# n2=[2,4,6,8]
# i=0
# a=[]
# b=[]
# while (i<len(n1)-1):
#     if (i<len(n1)-1):
#         a.append(n1[i+1]-n1[i])
#     if (i<len(n2)-1):
#         b.append(n2[i+1]-n2[i])
#     i+=1
# print(a)
# print(b)

# a=[4,5,5,5,3,8]
# i=0
# b=[]
# while i<len(a):
#     k=3
#     k1=2
#     while i<len(a):
#         if a[i]==a[i]:
#             k1+=1
#             i+=1
#         if k1>1:
#             b.append(a[i] )
#         i+=1
#         print(b)       
            


# num=int(input("enter the number"))
# a=1
# while a<=num:
#     i=1
#     count=0
#     while i<=a:
#         if(a%i==0):
#             count+=1
#         i+=1
#     if(count==2):
#         print(a,"prime number")
#     else:
#         print(a,"consonant number")
#     a+=1     


# i=4
# while i>=0:
#     b=1
#     while b<=i-1:
#         print("",end="")
#         b+=1
#     j=5
#     while j>i:
#         print(chr(64+j-i),end=" ")
#         j=j-1
#     print()
#     i-=1



# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")    
#         j+=1
#     k+=2  
#     print()    
#     i+=1

# a=[1,2,[3,4],[5,6]]
# b=[] 
# i=0 
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])==list:
#                 k=0 
#                 while k<len(a[i][j]): 
#                     b.append(a[i][j][k]) 
#                     k+=1 
#             else: 
#                 b.append(a[i][j])
#             j=j+1 
#     else:
#         b.append(a[i]) 
#     i=i+1 
# s=0 
# l=0 
# while l<len(b):
#     s+=b[l] 
#     l+=1 
# print(s)


# a=[1,2,[3,4],[5,6]]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i+=1
# print(sum)


# x="nitin"
# y=""
# for i in x:
#     y=i+y
# if y==x:
#     print("yes",y,"is palindrome")
# else:
#     print("not",y,"is not a palindrome")
  


# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j=j+1
#     k+=1    
#     print()
#     print()
#     i+=1        


# a=14
# b=12
# print(a^b)



# n=[[8,3,4,],
# [1,5,9],
# [6,7,2]]
# r1=0
# r2=0
# r3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         if i==0:
#             r1=r1+n[i][j]
#         elif i==1:
#             r2=r2+n[i][j]
#         else:
#             r3=r3+n[i][j]
#         i+=1
#     j+=1
# if r1==r2==r3:
#     print("row1",r1)
#     print("row2",r2)
#     print("row3",r3)
# else:
#     print("not equal",r1,r2,r3)
# c1=0
# c2=0
# c3=0
# i=1
# while i<len(n):
#     j=0
#     while j<len(n):
#         if i==0:
#             c1=c1+n[i][j]
#         elif i==1:
#             c2=c2+n[i][j]
#         else:
#             c3=c3+n[i][j]
#         i+=1
#     j+=1
# if c1==c2==c3:
#     print("column1",c1)
#     print("column2",c2)
#     print("column3",c3)
# else:
#     print("not",c1,c2,c3)



# a=[2,4,7,8,66,55]
# # o/p [2,4,6655]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     if j<len(a):# numbers.sort()
# print(numbers[-2])

# a=["delhi","gujarat","rajasthan","punjab","kerala"]
# a.reverse()
# print(a)


# a=["to get a job","to buy a house","to buy a car","to settle in a highest position","study hard"]
# for i in a:
#     print(i)

# a=["oil","sugar","maggi","mustard seeds","ground nuts","shampoos","soaps"]
# for i in a:
#     print(i)


# a=["oil","sugar","maggi","mustard seeds","ground nuts","shampoos","soaps","salt"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=[40,70,60,20,50]
# l=len(a)
# for i in range(l):
#     print(a[i])

# a=[40,70,60,20,50]
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i=i+1


# a=["wake up early in the morning","brushing after wake up","praying to god","respecting parents"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=["wake up early in the morning","brushing after wake up","praying to god","respecting parents"]
# [print(i) for i in a]

# a=["python","javascript","HTML","graphic design"]
# l=len(a)
# for i in range(l):
#     print(a[i])


# a=[50,40,23,70,56,12,5,10,7]
# i=0
# for j in a:
#     i+=1
# print(i)


# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# c=0
# while i<len(numbers):
#     a=numbers[i]
#     if a>=20 and a<=40:
#         c+=1
#     i+=1
# print(c)

# a=["n","i","t","i","n"]
# # a=["m","a","n","a","s","a"]
# b=a[-1::-1]
# if b==a:
#     print("palindrome")
# else:
#     print("not a palindrome")


# a=[1,0,0,1,1,0,1,1]
# i=0
# s=0
# while i<len(a):
#     s=s+a[-(i+1)]*2**i
#     i=i+1
# print(s)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)


# l1=[10,20,30,40]
# l2=[100,200,300,400]
# b=l2[::-1]
# i=0
# while i<len(l1):
#     print(l1[i],b[i])
#     i=i+1


# A=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# k=[]
# s=[]
# i=0 
# while i<len(A):
#     if type(A[i])==int:
#         k.append(A[i])
#     else:
#         s.append(A[i])
#     i=i+1
# print(k)
# print(s)


# a=[1,2,2,3,4,5]
# i=0
# b=[]
# while i<len(a)-1:
#     if a[i]<=a[i+1]:
#         b.append(a[i+1])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b) 


# a=[0,9,5]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1


# a=[1,2,[3,2,[5,6],3,[4]],89,80]
# b=[] 
# i=0 
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])==list:
#                 k=0 
#                 while k<len(a[i][j]): 
#                     b.append(a[i][j][k]) 
#                     k+=1 
#             else: 
#                 b.append(a[i][j])
#             j=j+1 
#     else:
#         b.append(a[i]) 
#     i=i+1 
# s=0 
# l=0 
# while l<len(b):
#     s+=b[l] 
#     l+=1 
# print(s)



# l1=[1,2,3,4,5,6]
# l2=[2,3,1,0,6,7]
# i=0
# while i<len(l1):
#     if l1[i] not in l2:
#         print(l1[i])
#     i+=1


# a=[1,2,3,4,5,6]
# b=[2,3,1,0,6,7]
# for i in a:
#     if i not in b:
#         print(i)



# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# b=0
# while i<3:
#     s=marks[0][b]+marks[1][b]+marks[2][b]
#     i+=1
#     b+=1
#     print(s)


# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# b=0
# for i in range(5):
#     s=marks[0][b]+marks[1][b]+marks[2][b]
#     b+=1
#     print(s)


# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# b=0
# s1=0
# s2=0
# s3=0
# while i<5:
#     s1= a[0][b]+s1
#     s2=a[1][b]+s2
#     s3=a[2][b]+s3
#     i+=1
#     b+=1
# print(s1/5)
# print(s2/5)
# print(s3/5)
# print("total marks for 3 years is :",s1+s2+s3)

# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len([a[i]]):
#         s+=a[i][j]
#         j+=1
#     i+=1
# print(s)


# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len([a[i]]):
#         s+=a[i][j]
#         j+=1
#     i+=1
# print(s)


# a=30
# n=[10,11,12,13,16,17,18,19]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if n[i]+n[j]==a:
#             print([n[i],n[j]])
#         j+=1
#     i+=1



# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num:",a[i])
#     else:
#         print("odd num:",a[i])
#     i=i+1

# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num:",a[i])
#         sum_even=sum_even+a[i]
#     else:
#         print("odd num:",a[i])
#         sum_odd=sum_odd+a[i]
#     i=i+1
# print("even sum",sum_even)
# print("odd sum",sum_odd)


# a=[23,14,56,12,19,9,15,23,31,42,43]
# i=0
# ec=0
# oc=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         sum_even=sum_even+a[i]
#         ec+=1
#     else:
#         sum_odd=sum_odd+a[i]
#         oc+=1
#     i=i+1
# print("even avg",sum_even/ec)
# print("odd avg",sum_odd/oc)
# print("total marks for 3 years is:",sum_even+sum_odd


# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# avg_even=0
# sum_even=0
# sum_odd=0
# b=len(a)
# while i<len(a):
#     if a[i]%2==0:
#         print("even num",a[i])
#         sum_even=sum_even+a[i]
#     else:
#         print("odd num",a[i])
#         sum_odd=sum_odd+a[i]
#         i=i+1
#     print(sum_even)
#     avg_even=sum_even/b
#     print(avg_even)
#     print(sum_odd)
#     avg_odd=sum_odd/b
    # print(avg_odd/b)



# a=[1,1,2,3,4,4,5,1]
# b=[]
# i=0
# while i<len(a):
#     c=[]
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     c.append(a[i])
#     c.append(count)
#     if  c not in b:
#         b.append(c)
#     i+=1
# print(b)        
    




# n1=[1,2,3,4,5,6,7,8,9,10]
# n2=[2,4,6,8]
# i=0
# a=[]
# b=[]
# while (i<len(n1)-1):
#     if (i<len(n1)-1):
#         a.append(n1[i+1]-n1[i])
#     if (i<len(n2)-1):
#         b.append(n2[i+1]-n2[i])
#     i+=1
# print(a)
# print(b)

# a=[4,5,5,5,3,8]
# i=0
# b=[]
# while i<len(a):
#     k=3
#     k1=2
#     while i<len(a):
#         if a[i]==a[i]:
#             k1+=1
#             i+=1
#         if k1>1:
#             b.append(a[i] )
#         i+=1
#         print(b)       
            


# num=int(input("enter the number"))
# a=1
# while a<=num:
#     i=1
#     count=0
#     while i<=a:
#         if(a%i==0):
#             count+=1
#         i+=1
#     if(count==2):
#         print(a,"prime number")
#     else:
#         print(a,"consonant number")
#     a+=1     


# i=4
# while i>=0:
#     b=1
#     while b<=i-1:
#         print("",end="")
#         b+=1
#     j=5
#     while j>i:
#         print(chr(64+j-i),end=" ")
#         j=j-1
#     print()
#     i-=1



# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")    
#         j+=1
#     k+=2  
#     print()    
#     i+=1

# a=[1,2,[3,4],[5,6]]
# b=[] 
# i=0 
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])==list:
#                 k=0 
#                 while k<len(a[i][j]): 
#                     b.append(a[i][j][k]) 
#                     k+=1 
#             else: 
#                 b.append(a[i][j])
#             j=j+1 
#     else:
#         b.append(a[i]) 
#     i=i+1 
# s=0 
# l=0 
# while l<len(b):
#     s+=b[l] 
#     l+=1 
# print(s)


# a=[1,2,[3,4],[5,6]]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i+=1
# print(sum)


# x="nitin"
# y=""
# for i in x:
#     y=i+y
# if y==x:
#     print("yes",y,"is palindrome")
# else:
#     print("not",y,"is not a palindrome")
  


# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j=j+1
#     k+=1    
#     print()
#     print()
#     i+=1        





# a=[2,4,7,8,66,55]
# # o/p [2,4,6655]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     if j<len(a):
#         print(a)
#         b.append(a)
#     i+=1
# print(b)



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




