import random
import time

a = random.randrange(1, 9)
b = random.randrange(1, 9)
c = a*b

starttime = time.time()
print("구구단 게임을 시작합니다.")

print(a,'*',b ,"?")
result = int(input())
endtime = time.time()

if result ==c:
    print("정답입니다.",endtime -starttime,"초 걸렸습니다.")
else:
    print("오답입니다.")