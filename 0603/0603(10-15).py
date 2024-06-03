def input_num_of_population():
    nPeople=[]
    for f in range(4):
        n=int(input(f'{f+1}층의 거주인원수는? '))
        nPeople.append(n)
    return nPeople

def get_total(lst):
    total=0
    for n in lst:
        total +=n
    return total

def show_num_of_population(p):
    for i in range(4):
        print(f'{i+1}층의 거주인원수는 {p[i]}명입니다.')

population=input_num_of_population()

show_num_of_population(population)

total=get_total(population)

print(f'총 거주인원수는 {total}명입니다.')

