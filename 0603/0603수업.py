def show(p):
    n=len(p)
    for i in range(n-1,-1,-1):
        print(nums[i])

def input_list(n):
    lst=[]
    for i in range(n):
        v=int(input('? '))
        lst.append(v)
    return lst

nums = input_list(3)
show(nums)
