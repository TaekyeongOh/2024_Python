def input_list(lst):
    name=input('이름?')
    num = input('번호?')

    lst.append(name)
    lst.append(num)


userinfo = []
input_list(userinfo)
print(f'{userinfo[1]}번 {userinfo[0]}')
