#num=정수 하나를 입력받음
num=int(input("정수를 입력하세요"))

#if num이 짝수라면:
    #짝수라 출력

#else:
    #홀수라 출력

if num%2==0:
    print(f'{num}은(는) 짝수입니다.')

else:
    print(f'{num}은(는) 홀수입니다.')


if num%2==0:
    print('짝수', end='')

else:
    print('홀수', end='')

print('입니다.')
