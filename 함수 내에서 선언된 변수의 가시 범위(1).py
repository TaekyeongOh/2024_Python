def first():
    msg='안녕'
    print(msg)
    print(second())

def second():
    print('오태경')
    return '안녕하세요'

first()
