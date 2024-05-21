name=str(input('이름?'))
cut_name=name[1:]

if name=='':
    print('오류')
else:
    print(f'반가워요 {cut_name}님')
