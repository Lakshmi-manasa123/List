list1 = [2,-7,5,-64,-14]
pos_count=0
neg_count = 0
num = 0
while(num < len(list1)):
    if list1[num] >= 0:
        pos_count += 1
    else:
        neg_count += 1
    num += 1
print("Pos num in the list: ", pos_count)
print("Neg num in the list: ", neg_count)


