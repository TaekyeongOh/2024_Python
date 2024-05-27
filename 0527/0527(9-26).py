d={'python':'파이썬','basic':'기초','programming':'프로그래밍'}

key='python'
if key in d:
    print(d[key])
else:
    print(f'오류: 유효하지 않은 키 {key}')
