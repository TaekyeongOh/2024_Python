# 20240960 오태경
# 10장 6번


def buy(shopping_bag):
    item=None
    while item != '':
        item = input('상품명? ')
        if item == '':
            print()
            break
        
        num = int(input('수량은? '))
        shopping_bag[item] = num
        print(f'장바구니에 {item}가(이) {num}개 담겼습니다.')
        print()

def show(shopping_bag):
    print('>>> 장바구니 보기:', shopping_bag)


shopping_bag = {}

print('[구입]')

buy(shopping_bag)
show(shopping_bag)

print()
search_item = input('장바구니에서 확인하고자 하는 상품은?')
if search_item in shopping_bag:
    print(f'장바구니에 {search_item}은(는) {shopping_bag[search_item]}개 담겨져 있습니다.')
else:
    print(f'장바구니에 {search_item}은(는) 없습니다.') 
