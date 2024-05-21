def is_even_number(n):
    if n%2 ==0:
        return True
    else:
        return False

num=int(input('정수를 입력하세요.'))

print(f'{num}은 ')

if is_even_number(num):
    print('짝수 ')
else:
    print('홀수 ')

print('입니다.')
