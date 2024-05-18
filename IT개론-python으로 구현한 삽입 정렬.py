def insertion(ds):
    for a in range(1,len(ds)):
        key=ds[a]
        b=a-1
        while b>=0 and ds[b]<key:
            ds[b+1]=ds[b]
            b=b-1
        ds[b+1]=key

dataset=[15, 12, 20, 17, 28]
insertion(dataset)
print(dataset)
