import random

# 사용자 정의 함수부
def get_operator():
    return random.randint(1,10)

def get_operand(operator):
    operand = random.randint(1,10)
    while operand>=operator:
        operand=random.randint(1,10)
    return operand

def show_quiz(operator,operand,r):
    if r==1: 
        plus = int(input(f'{operator}+{operand}='))
        return plus
    else:
        minus = int(input(f'{operator}-{operand}='))
        return minus
    
def get_answer(operator,operand,r):
    if r == 1:
        return operator+operand
    else:
        return operator-operand


# 주 프로그램
operator=get_operator()
operand=get_operand(operator)

r=random.randint(1,2)

user_input=show_quiz(operator,operand,r)
correct_answer=get_answer(operator,operand,r)

if user_input == correct_answer:
    print('정답입니다.')
else:
    print('오답입니다.')
