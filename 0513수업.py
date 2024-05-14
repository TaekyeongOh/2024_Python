def find_odd(s,e,m):
    # for n을 s부터 e까지 2씩 증가하면서 반복:
    for n in range(s,e,2):
        # if n이 홀수이면서 동시에 n이 m의 배수가 아니면:
        if (n%2==0) and (n%m==0):
            print(n)
                # print(n)

find_odd(start,end,dele)
start=input(int('시작값?'))
end=input(int('끝값?'))
dele=input(int('제외할 배수?'))
