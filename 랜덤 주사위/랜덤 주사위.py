import random
count = 0
eyes = 0
result=0
while True:
    count +=1
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    d5 = random.randint(1, 6)
    d6 = random.randint(1, 6)
    # 순서대로 주사위 눈이 1,2,3,4,5,6 이 나와야 하기 때문에 주사위에 첫번쩨부터 여섯번째 눈이 순서대로 1,2,3,4,5,6이 되면 된다.
    if d1 ==1 and d2 ==2 and d3 ==3 and d4 ==4 and d5 ==5 and d6 == 6:
        result=+1
    # 모든 주사위의 눈이 같을 때 브레이크를 한다.
    if d1 == d2 == d3 == d4 == d5 == d6:
        eyes = d1
        break

print("6개 모두 동일한 숫자가 나올때까지 주사위를 던진 횟수와 주사위의 눈:",count,",",eyes)
print("{}회 주사위를 던지는 동안 1,2,3,4,5,6 의 주사위가 나온 횟수:".format(count),result)