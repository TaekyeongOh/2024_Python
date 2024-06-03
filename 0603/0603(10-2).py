def input_list():
    name=input('이름? ')
    num=input('번호? ')

    lst=[]
    lst.append(name)
    lst.append(num)
    return lst

userinfo=input_list()
print(f'{userinfo[1]}번 {userinfo[0]}')
