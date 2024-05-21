# 사용자 정의 함수부
def get_integer():
    n=int(input("정수를 입력하세요."))
    return n

def diff(n1,n2):
    if n1==n2:
        d=0
    elif n1>n2:
        d=n1-n2
    else:
        d=n2-n1
    return d
    
#주 프로그램부

#n1=첫번째 정수 입력
n1=get_integer()
#n2=첫번째 정수 입력
n2=get_integer()
#d= n1과 n2의 차이를 계산
d=diff(n1,n2)
#d를 출력
print(f'{n1}과 {n2}의 차는 {d}')
