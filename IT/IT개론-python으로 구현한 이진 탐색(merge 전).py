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
print(binary(dataset,17))
