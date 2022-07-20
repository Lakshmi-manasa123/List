a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
min=a[0]
sec_max=0
sec_min=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]>sec_max and a[i]!=max:
        sec_max=a[i]
    if a[i]<min:
        min=a[i]
    if a[i]<sec_min and a[i]!=min:
        sec_min=a[i]
    i+=1
print(max)
print(sec_max)
print(min)
print(sec_min)