n =int(input("몇진수를 10진수로 바꿀예정이신가요? :"))
v =list(str(input("{0} 진수 숫자를 입력하세요:".format(n))))
# v를 역순으로 바꾼다.
v.reverse()
sum=0
s =1 
for i in v:
    if int(i) >= n:
        print("주어진 수는 {}진수 수가 아닙니다.".format(n))
        sum=-1
        break
        
    sum += int(i)*s
    s=n*s
if sum!=-1:
    print("10 진수로 바꾼 결과입니다.:",sum)
