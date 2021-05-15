# 연속적인 구구단 계산기
print("종료 하시려면 0을 입력하세요")
print("구구단 몇 단을 계산할까여(1~9)?")

while True:
    x = int(input())

    if x == 0:
        break
    if not (1 <= x <= 9):
        print("잘못 입력했습니다.", "1부터 9 사이 숫자를 입력하세요.")
        continue
    else:
        print("구구단" + str(x) + "단을 계산합니다.")
        for i in range(1, 10):
            print(str(x) + "x" + str(i) + "=" + str(x * i))
        print("구구단 몇 단을 계산할까요(1~9)?")
print("구구단 게임을 종료합니다.")
