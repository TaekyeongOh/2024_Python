def sel(ds):
    for a in range(0,len(ds)-1):
        min_ind=a
        for b in range(a+1,len(ds)):
            if ds[b]<ds[min_ind]:
                min_ind=b
        ds[a], ds[min_ind] = ds[min_ind],ds[a]
    return ds

def binary(ds,key):
    low=0
    high=len(ds)-1
    while low<=high:
        mid=(low+high)//2
        if key==ds[mid]:
            return mid
        elif key<ds[mid]:
            high=mid-1
        else:
            low=mid+1
    return

dataset=[15,12,20,17,28]
get_set=sel(dataset)
print(binary(get_set,17))
