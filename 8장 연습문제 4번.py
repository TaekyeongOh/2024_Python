# 20240960 / 오태경
# 8장 연습문제 4번


#--------------------
# 사용자 정의 함수부
def is_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False


#--------------------
# 주 프로그램부
ans='y'
while ans=='Y' or ans=='y':
    year=int(input('윤년 여부를 확인할 연도는? '))
    if is_leap_year(year):
        print(f'{year}년은 윤년입니다.')
    else:
        print(f'{year}년은 평년입니다.')
    ans=str(input('다른 연도를 확인하겠습니까?'))
