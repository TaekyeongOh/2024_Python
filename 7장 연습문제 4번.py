# 20240960 / 오태경
# 7장 연습문제 4번


#--------------------
# 사용자 정의 함수부

# 나이 입력받는 함수 input_age() 정의하기
def input_age():
    age=int(input('나이?'))
    if 0<= age <=120:
        return age
    else:
        return -1

# 나이를 인수로 잔달받아 성인여부 판별해주는 함수 is_adult() 정의하기
def is_adult(age):
    if  age <= 18:
        return False
    else:
        return True


#--------------------
# 주 프로그램부
age=input_age()
if age!=-1:
    if is_adult(age)==False:
        print('당신은 미성년자입니다.')
    else:
        print('당신은 성인입니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')
    
    
    
