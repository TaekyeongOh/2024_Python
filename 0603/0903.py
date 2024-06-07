shopping_bag = []
item = []

print('[구입]')

while item != '':
    # item = 상품 이름을 입력받기
    item = str(input('상품명? '))
    # item이 빈 문자열이면 루프 빠져 나가기
    if item != '':
        # item을 장바구니에 추가하기
        shopping_bag.append(item)
        print(f'장바구니에 {item}가(이) 담겼습니다.')
        print()

# 장바구니의 모든 상품 이름 출력하기
print('>>> 장바구니 보기:', shopping_bag)
