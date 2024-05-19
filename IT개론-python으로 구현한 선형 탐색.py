def linear(ds,key):
    for a in range(0,len(ds)):
        if key == ds[a]:
            return a
    return

dataset=[15,12,20,17,28]
sorted_ds=sorted(dataset)
print(linear(sorted_ds,17))
