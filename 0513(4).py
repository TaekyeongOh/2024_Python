# 사용자 정의 함수부
def start_odd():
    if start%2==1:
        return start
    else:
        return int(start+1)

def end_odd():
    if end%2==1:
        return end+1
    else:
        return end
    

def find_odd():
    for num in range(start,end,2)




# 주 프로그램 부

# 시작값을 입력받음
start=input(int('시작값?'))
# 끝값을 입력받음
end=input(int('끝값?'))
# 제외할 배수를 입력받음
dele=input(int('제외할 배수?'))
# 홀수 중에서 시작값~끝값, 특정 배수 제외해서 출력
