def dict_get(dic,key):
    if key in dic:
        return dic[key]
    else:
        return None

d={'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

res=dict_get(d,'python')
if res != None:
    print(res)
else:
    print('오류: 잘못된 키')

res=dict_get(d,0)
if res!=None:
    print(res)
else:
    print('오류: 잘못된 키')
