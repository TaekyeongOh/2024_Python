# 20240960 / 오태경
# 8장 연습문제 5(2)번


#--------------------
# 사용자 정의 함수부
def rec(hei):
    for i in range(1,hei+1):
        for j in range(hei-i, 0,-1):
            print(' ', end="")
        for j in range(1,i+1):
            print('*', end='')
        print()



#--------------------
# 주 프로그램부
hei=int(input('높이?'))
rec(hei)
