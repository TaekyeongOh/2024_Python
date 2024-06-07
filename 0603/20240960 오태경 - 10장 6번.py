# 20240960 오태경
# 10장 문제 6번


def buy():
    shopping_bag = {}
    item = None
    while item != '':
        item = input('상품명? ')
        if item != '':
            shopping_bag.append(item)
            print(f'장바구니에 {item}가(이) 담겼습니다.')
    return shopping_bag


# 물건 구매
print('[구입]')
shopping_bag = buy()

# 구매 완료 후 쇼핑백 출력
print(f'>>> 장바구니 보기: {shopping_bag}')
