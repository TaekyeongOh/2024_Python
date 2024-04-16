import random

problems=['사자', '개', '호랑이', '토끼', '고양이']
answers=['lion', 'dog', 'tiger', 'rabbit', 'cat']

for a in range(len(problems)):
    index=random.randint(0,len(problems)-1)
    print(problems[index],end=' ')
    ans=input('-->')
    if ans==answers[index]:
        print('맞습니다.')
    else:
        print('틀렸습니다.')
    del(problems[index])
    del(answers[index])
