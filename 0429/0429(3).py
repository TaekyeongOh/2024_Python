# 주 프로그램부

#score=점수를 입력받음
score=int(input("점수를 입력하시오:"))

#grade=점수(score)에 따른 학점 판별

def get_grade(score):
    if 80 < score <= 100:
        grade = "A"
    elif 60 < score:
        grade = "B"
    elif 40 < score :
        grade = "C"
    elif 20 < score:
        grade = "D"
    else:
        grade = "F"
    return grade

#입력된 점수에 대한 학점을 출력
print(f'{score}점이므로 학점은 {get_grade(score)}입니다.')
