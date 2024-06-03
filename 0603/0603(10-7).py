# 인구조사 프로그램의 의사 코드
#_________________________________


# 사용자 정의 함수부
def input_num_of_population():
    # 리스트 nPeople 선언
    nPeople = []
    # for f를 1부터 4까지 변화하면서
    for f in range(4):
        n=int(input(f'{f+1}층의 거주인원수는? '))
        nPeople.append(n)
        # nPeople[f-1] = f층의 거주인원수를 입력받음
    return nPeople

def show_num_of_population(p):
    f=1
    for n in p :
        print(f'{f}층의 거주인원수는 {n}명입니다.')
        f +=1

def get_total(lst):
    total = lst[0] + lst[1] + lst[2] + lst[3]
    return total
        

# 1~4층의 거주인원수를 입력받음
population=input_num_of_population()

# 입력받은 1~4층의 거주인원수를 출력
show_num_of_population(population)

# total = 입력받은 1~4층의 거주인원수의 총합을 구함
total = get_total(population)

# 총 거주인원수(total) 출력
print(f'총 거주인원수는 {total}명입니다.')
