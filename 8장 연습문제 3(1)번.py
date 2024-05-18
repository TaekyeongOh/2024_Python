# # 20240960 / 오태경
# 8장 연습문제 3(1)번


#--------------------
# 사용자 정의 함수부
def find_start(start):
    if start%2==1:
        return start
    else:
        return start+1


def find_end(end):
    if end%2==1:
        return end
    else:
        return end-1

def find_odd(start,end,odd):
    for i in range(start,end+1,2):
        if i % odd != 0:
            print(i, end=' ')
    

#--------------------
# 주 프로그램부
start=int(input('시작값?'))
end=int(input('끝값?'))
odd=int(input('제외할 배수?'))

start=find_start(start)
end=find_end(end)
find_odd(start,end,odd)
