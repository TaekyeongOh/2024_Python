# 20240960 / 오태경
# 7장 연습문제 2번


#--------------------
# 사용자 정의 함수부


# 연도를 year로 전달받아 윤년이면 True, 윤년이 아니면 False를 반환하는 함수 작성
def is_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

# 연도와 월을 입력받아 그 달의 끝날이 며칠인지를 반환하는 함수 작성
def month_days(year,month):
    # 2월을 선택했을 경우
    if month==2:
        if is_leap_year(year):
            print(f'{year}년 2월은 29일',end='')
        else:
            print(f'{year}년 2월은 28일',end='')
            
    # 1,3,5,7,8,10,12월을 선택했을 경우
    elif (month==1) or(month==3) or(month==5) or(month==7) or(month==8) or(month==10) or(month==12):
        print(f'{year}년 {month}월은 31일',end='')
        
    # 1,2,3,5,7,8,10,12월을 선택하지 않았을 경
    else:
        print(f'{year}년 {month}월은 30일',end='')
    print('까지 있습니다.')

#--------------------
# 주 프로그램부

# year = 연도 묻기
year=int(input('연도?'))

# month = 월 묻기
month=int(input('월?'))

is_leap_year(year)
month_days(year,month)
