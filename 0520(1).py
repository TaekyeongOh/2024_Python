import random

# 사용자 정의 함수부
def get_operator():
    return random.randint(1,11)

def get_operand(operator):
    operand=0
    while operand>=operator:
        operand=random.randint(1,11)
    return operand

def show_quiz(operator,operand):
    r=random.randint(0,1)
    if r==0: 
        plus = int(input(f'{operator}+{operand}='))
        return plus
    else:
        minus = int(input(f'{operator}-{operand}='))
        return minus
    
def get_answer(plus,minus):
    if show_quiz(operator,operand) == plus:
        return operator+operand
    if show_quiz(operator,operand) == minus:
        return operator-operand


# 주 프로그램
operator=get_operator()
operand=get_operand()
if show_quiz(operator,operand) == get_answer(plus,minus):
    print('정답입니다.')
else:
    print('오답입니다.')

