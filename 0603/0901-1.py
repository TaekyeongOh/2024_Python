score = []

# 3번 반복하여 사용자로부터 점수를 입력받아 리스트에 추가합니다.
for i in range(3):
    # 사용자로부터 점수를 입력받습니다. 입력받은 값은 문자열이므로 정수로 변환합니다.
    s = int(input(f'#{i+1}? '))
    # 리스트 score에 입력받은 점수를 추가합니다.
    score.append(s)

# 입력받은 점수를 출력합니다.
print('입력받은 점수:', score)

average=sum(score)/len(score)

print('평균: ',average)
