def input_scores():
    scores = []
    s = 0  
    while s >= 0: 
        s = float(input(f'#{len(scores) + 1}? '))
        if s >= 0:
            scores.append(s)
    return scores

def get_average(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average

# 리스트 scores에서 학생들의 점수를 입력받기
print('[점수 입력]')
scores = input_scores()

# avg = scores의 저장된 점수의 평균을 구하기
avg = get_average(scores)

# scores의 각 학생들 점수와 평균 avg를 출력하기
print()
print('[점수 출력]')

print(f'개인 점수: {scores}')
print(f'평균: {avg:.1f}')
