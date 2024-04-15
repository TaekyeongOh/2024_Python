# 사용자 정의 함수부

def rep_char(length):
    print(f'{'-'*int(2*length*n)}')

def draw_line_string(c,n):
    rep_char(length)
    print(f'{c*int(n)}')
    rep_char(length)

# 본 프로그램부

c=input("문자를 입력하세요.")
n=int(input("입력한 정수를 몇 번 반복할까요?"))
length=int(len(c))
draw_line_string(c,n)
