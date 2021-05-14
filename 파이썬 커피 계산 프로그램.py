print("주문 할 음료를 말씀하세요.")
americano = int(input("아메리카노(잔) :"))
latte = int(input("카페라테(잔) :"))
cappuccino= int(input("카푸치노(잔) :"))
money= int(input("지불하실 금액을 입력하세요 :"))

total= (2500*americano)+ (3000*latte)+ (3000* cappuccino)
changes = money -total

if changes>=0:
    print("잔돈은",changes,"원입니다.")
else:
    print("현금을 더 넣어주세요")