# 리스트 scores에서 세 학생의 점수를 입력받기
print('[점수 입력]')

score=[]

for a in range(3):
    s=int(input(f'#{a+1}? '))
    score.append(s)
    
print()
print('[점수 출력]')
print('입력 점수: ',score)
# avg = scores의 저장된 점수의 평균을 구하기
average=sum(score)/len(score)
# scores의 각 학생 점수와 평균 avg를 출력하기
print('평균: ',average)
