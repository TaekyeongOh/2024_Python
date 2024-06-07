shopping_bag = []
item = []

print('[구입]')

while item != '':
    item = str(input('상품명? '))
    if item != '':
        shopping_bag.append(item)
        num=int(input('수량은? '))
        print(f'장바구니에 {item}가(이) {num}개 담겼습니다.')
        print()

print(f'>>> 장바구니 보기: {shopping_bag}:{num}')
