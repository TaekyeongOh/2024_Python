# 사용자 정의 함수부
def input_positive_number(prompt):
    n=0
    while n <=0:
        n = int(input(prompt))

    return n

def display_multiplication_table(n):
    for i in range(1,10):
        print(f'{n}x{i}={n*i:2d}')


# 주 프로그램부
# n = 사용자로부터 양의 정수를 입력받음
n = input_positive_number('출력할 구구단을 양의 정수로 입력하세요: ')

# n에 대한 구구단표를 출력
display_multiplication_table(n)
