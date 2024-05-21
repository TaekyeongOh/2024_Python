# 20240960 / 오태경
# 8장 연습문제 2번


#--------------------
# 사용자 정의 함수부

def read_single_digit(get_int):
    if get_int==1:
        print('일',end=' ')
    elif get_int ==2:
        print('이',end=' ')
    elif get_int ==3:
        print('삼',end=' ')
    elif get_int ==4:
        print('사',end=' ')
    elif get_int ==5:
        print('오',end=' ')
    elif get_int ==6:
        print('육',end=' ')
    elif get_int ==7:
        print('칠',end=' ')
    elif get_int ==8:
        print('팔',end=' ')
    elif get_int ==9:
        print('구',end=' ')
    else:
        print('영',end=' ')


    
# 임의 자릿수 정수를 입력받아도 처리 가능하도록 함수 작성
def read_number():
    get_int = input('양의 정수 입력: ')
    get_len = len(get_int)
    order=0
    
    while order!=get_len:
        num=int(get_int[order])
        read_single_digit(num)
        order+=1
    
    
    

#--------------------
# 주 프로그램부
read_number()


