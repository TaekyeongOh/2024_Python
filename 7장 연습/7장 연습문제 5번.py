# 20240960 / 오태경
# 7장 연습문제 5번


#--------------------
# 사용자 정의 함수부

# 입력받은 문자가 숫자인지 확인하는 함수 생성
def is_num(now_in):
    if now_in.isdigit():
        return True
    else:
        return False

# 입력받은 문자가 알파벳인지 확인하는 함수 생성        
def is_al(now_in):
    if now_in.isalpha():
        return True
    else:
        return False

# 입력받은 문자가 스페이스 공백인지 확인하는 함수 생성
def is_sp(now_in):
    if (now_in==' '):
        return True
    else:
        return False
        
# 입력받은 문자가 탭인지 확인하는 함수 생성
def is_tab(now_in):
    if (now_in== '    '):
        return True
    else:
        return False
        

#--------------------
# 주 프로그램부

# 한 문자 입력받기
now_in = input('한 문자 입력?')

if is_num(now_in):
    print('숫자',end=' ')
elif is_al(now_in):
    print('알파벳',end=' ')
elif is_sp(now_in):
    print('스페이스 공백',end=' ')
elif is_tab(now_in):
    print('탭',end=' ')
else:
    print('기타',end=' ')

print('문자를 입력했습니다.')
