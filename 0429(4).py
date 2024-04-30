# 사용자 정의 함수부
def is_leap_year(y):
    if (y%4 ==0 and y%100!=0) or (y%400==0):
        return True
    else:
        return False

# 주 프로그램부
# year=연도를 입력받음
year=int(input("윤년 여부 확인 연도는?"))

print(f'{year}년은', end=' ')
if is_leap_year(year):
    print("윤년입니다.")

else:
    print("평년입니다.")
