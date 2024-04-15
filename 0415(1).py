# 사용자 정의 함수부
def divide_name(name) :
    global s
    s = name[0]
    global n
    n = name[1:]

# 주 프로그램 부
# name = 사용자로부터 이름을 입력 받음
name = input('당신의 이름은?')

# 입력된 이름 (name)에서 성과 이름을 분리하여 출력
divide_name(name)
print("성:",s)
print("이름:",n)
