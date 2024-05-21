for a in range(10):
    for b in range(1,11):
        print(b, end=' ')
    print()


num=int(input('숫자?'))
add=1
for a in range(num):
    while add!=num:
        for b in range(1,num+1):
            print(b, end=' ')
        add+=1
        print()
