shopping_bag = {}

print('[구입]')

item = None  # 초기화

while item != '':
    # item = 상품 이름을 입력받기
    item = input('상품명? ')
    # item이 빈 문자열이면 루프 빠져 나가기
    if item == '':
        print()
        break
    
    # item을 장바구니에 추가하거나 수량 증가시키기
    num = int(input('수량은? '))
    shopping_bag[item] = num
    print(f'장바구니에 {item}가(이) {num}개 담겼습니다.')
    print()

# 장바구니의 모든 상품 이름과 수량을 한 줄에 출력하기
print('>>> 장바구니 보기:', shopping_bag)

# 장바구니에서 확인하고자 하는 상품 검색
print()
search_item = input('장바구니에서 확인하고자 하는 상품은?')
if search_item in shopping_bag:
    print(f'장바구니에 {search_item}은(는) {shopping_bag[search_item]}개 담겨져 있습니다.')
else:
    print(f'장바구니에 {search_item}은(는) 없습니다.') 
