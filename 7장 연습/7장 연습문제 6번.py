# 20240960 / 오태경
# 7장 연습문제 6번


#--------------------
# 사용자 정의 함수부

# 한 자리 10진 정수에 대한 한글 문자열을 반환하는 함수 작성
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

    
# 세 자리 10진 정수에 대한 한글을 문자열로 반환하는 함수 작성
def read_number():
    # 세 자리 정수 입력받기
    get_int = str(input('세 자리 정수 입력: '))
    # fir=입력받은 세 자리 정수 중 첫 정수
    fir = int(get_int[0])
    read_single_digit(fir)
    # sec=입력받은 세 자리 정수 중 두 번째 정수
    sec = int(get_int[1])
    read_single_digit(sec)
    # thi=입력받은 세 자리 정수 중 세 번째 정
    thi = int(get_int[2])
    read_single_digit(thi)

#--------------------
# 주 프로그램부
read_number()

