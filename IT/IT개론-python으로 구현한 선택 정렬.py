def sel(ds):
    for a in range(0,len(ds)-1):
        min_ind=a
        for b in range(a+1,len(ds)):
            if ds[b]>ds[min_ind]:
                min_ind=b
        ds[a], ds[min_ind] = ds[min_ind],ds[a]

dataset=[15,12,20,17,28]
sel(dataset)
print(dataset)
