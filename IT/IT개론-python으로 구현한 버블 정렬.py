def bubble(ds):
    for a in range(0,len(ds)-1):
        for b in range(0,len(ds)-1-a):
            if ds[b]<ds[b+1]:
                ds[b], ds[b+1]=ds[b+1],ds[b]

dataset=[15, 12, 20, 17, 28]
bubble(dataset)
print(dataset)
