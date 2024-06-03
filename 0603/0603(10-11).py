def input_num_of_population():
    nPeople=[0,0,0,0]
    for f in range(1,5):
        nPeople[f-1]=int(input(f'{f}층의 거주인원수는? '))
    return nPeople

def get_total(lst):
    total=lst[0]+lst[1]+lst[2]+lst[3]
    return total

def show_num_of_population(p):
    cnt=len(p)
    for i in range(cnt):
        print(f'{i+1}층의 거주인원수는 {p[i]}명입니다.')

population=input_num_of_population()

show_num_of_population(population)

total=get_total(population)

print(f'총 거주인원수는 {total}명입니다.')
