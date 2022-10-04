lst = [1,8,6,2,5,9,5,3,8]
maxS = 0
maxHeight = 0
lenOf = 0
for i in range(len(lst)):
    for y in range(len(lst)):
        if i != y:
            if lst[i] < lst[y]:
                maxHeight = lst[i]
            if lst[i] > lst[y]:
                maxHeight = lst[y]
            if lst[i] == lst[y]:
                maxHeight = lst[i]
                # lenOf =
            if maxHeight*maxHeight*(lst[i]+1) > maxS:
                maxS = maxHeight*maxHeight*(lst[i]+1)
                z = lst[i]
                zIndex = i
                z1= lst[y]
                z1Index = y
print(maxS)
print(maxHeight)
print(f'По индексу: {zIndex}, число {z}')
print(f'По индексу: {z1Index}, число {z1}')