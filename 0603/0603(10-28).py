def dict_append(dic,key,value):
    if key in dic:
        return False

    dic[key] = value
    return True

d={'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

if dict_append(d,'PYTHON','파이썬'):
    print('추가 성공')
else:
    print('추가 실패')

if dict_append(d, 'basic','베이직'):
    print('두 번째 추가 성공')
else:
    print('두 번째 추가 실패')

print(d)
