def maxList(listA):
    m=listA[0]
    for a in range(1,len(listA)):
        if listA[a]>m:
            m=listA[a]
    return m

listB=[30,70,50, 20, 10, 80, 100]
print('최댓값: ', maxList(listB))
