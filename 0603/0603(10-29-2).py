def dict_delete(dic,key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

d={'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}
if dict_delete(d,'basic'):
    print('삭제 성공')
else:
    print('삭제 실패')

print(d)
