# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print(numbers[-2])


a=[50,40,23,70,56,12,5,10,7]
# a=[23,45,67,78,89,90,21]
i=0
max=0
sec_max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]>sec_max and a[i]!=max:
        sec_max=a[i]
    i+=1
print(max)
print(sec_max)
