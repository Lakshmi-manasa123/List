list2=[-12,14,95,3]
pos_count=0
neg_count=0
i=0
while (i<len(list2)):
    if list2[i]>=0:
        pos_count+=1
    else:
        neg_count+=1
    i   +=1
print("pos num in the list:",pos_count)
print("neg num in the list:",neg_count)
