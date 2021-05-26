class Basket(object):

    def __init__(self, id):
        self.id = id
        self.items = [] # 구매한 물건 이름
        self.prices = [] # 구매한 물건의 가격
        self.quantity = [] # 구매한 물건의 개수
        self.total = 0 # 전체 가격
        self.notime = 0 # 물건의 종류

    def add(self, name, prices, quantity):
        self.items.append(name) # 구매한 물건 추가
        self.prices.append(prices) # 구매한 물건의 가격 추가
        self.quantity.append(quantity) # 구매한 물건의 개수 추가
        self.total += prices * quantity # 가격 * 개수를 전체 가격에다가 더한다.
        self.notime += 1 # 물건의 종류는 1개를 더한다.

    def delete(self, name, prices, quantity):
        self.items.remove(name) # 구매한 물건 삭제
        self.prices.remove(prices) # 구매한 물건의 가격 삭제
        self.quantity.remove(quantity) # 구매한 물건의 개수 삭제
        self.total -= prices * quantity # 가격 * 개수를 전체 가격에서 뺀다.
        self.notime -= 1 # 물건의 종류는 1개를 삭제한다.

    def print(self):
        for i in range(len(self.items)):
            print("{0}님의 장바구니 물건의 종류에는 {1}(이)가 있고 {1}의 갯수는 {2}개가 있다.".format(self.id ,self.items[i], self.quantity[i]))

        return ("따라서 {0}님의 총 장바구니 물건의 종류는 {1}(이)가 있고 물건의 갯수는 각{2}개 이고 총 금액은 {3}원이고 총 물건의 종류의 갯수는 {4}개이다."
              .format(self.id, self.items, self.quantity, self.total, self.notime))



shopping = Basket("조준장")
shopping.add("바지", 10000, 2)
shopping.add("윗 옷", 10000, 2)
shopping.add("신발", 10000, 2)
shopping.delete("신발", 10000, 2)