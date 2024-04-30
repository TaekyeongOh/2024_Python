#사용자 정의 함수부
#odd=시작값과 끝값 사이의 홀수 저장하기
def check_odd(start):
    if start%2==0:
        start_odd=start+1
    else:
        start_odd=start
    return start_odd

#print_num=odd와 제외 배수 값의 여집합 저장하기
def print_num(times,start_odd,end):
    nnum=times



#시작값이 무엇인지 묻기
start=int(intput("시작값이 무엇인가요?"))

#끝값이 무엇인지 묻기
end=int(input('끝값이 무엇인가요?'))

#제외할 배수 묻기
times=int(input('제외할 배수가 무엇인가요?'))

#print_num print하기
