import random

# 사용자 정의 함수부
def get_operator():
    return random.randint(1, 10)

def get_operand(operator):
    operand = random.randint(1,10)
    while operand >= operator:
        operand = random.randint(1, 10)
    return operand

def show_quiz(operator, operand):
    r = random.randint(1, 2)
    if r == 1:
        user_input = int(input(f'{operator} + {operand} = '))
        return user_input, r
    else:
        user_input = int(input(f'{operator} - {operand} = '))
        return user_input, r

def get_answer(operator, operand, r):
    if r == 1:
        return operator + operand
    else:
        return operator - operand

# 주 프로그램
operator = get_operator()
operand = get_operand(operator)

user_input, r = show_quiz(operator, operand)
correct_answer = get_answer(operator, operand, r)

if user_input == correct_answer:
    print('정답입니다.')
else:
    print('오답입니다.')
