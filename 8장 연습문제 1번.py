#사용자 정의 함수부

def input_age():
    age=int(input('나이?'))
    while age<=0 or age>120:
        age=int(input('나이?'))
    return age

# 주 프로그램부
age=input_age()
if age>18:
    print('당신은 성인입니다.')
    
elif 0<age<=18:
        print('당신은 성인이 아닙니다.')
