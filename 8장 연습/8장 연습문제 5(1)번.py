# 20240960 / 오태경
# 8장 연습문제 5(1)번


#--------------------
# 사용자 정의 함수부
def rec(hei):
    for a in range (1, hei+1):
        for b in range (1, a+1):
            print(b, end='')
        print()


#--------------------
# 주 프로그램부
hei = int(input('높이?'))
rec(hei)
