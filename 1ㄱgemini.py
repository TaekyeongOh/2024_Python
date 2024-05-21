hei=int(input('높이?'))

for i in range(1,hei+1):
    for j in range(hei-i, 0,-1):
        print(' ', end="")
    for j in range(1,i+1):
        print('*', end='')
    print()
