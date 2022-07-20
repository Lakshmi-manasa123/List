# import numbers


# a=[50,40,23,70,56,12,5,10,7]
a=[[1,2,3],[4,5,6],[8,9,10]]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i+=1
print(min)


# a=[2,3,4,[2,3],7,8,[5,6,7,[5,7,9],7,2]]
# a.remove(4)
# print(a)