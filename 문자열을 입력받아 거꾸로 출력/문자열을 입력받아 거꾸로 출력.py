#리스트로 문자열을 받는다.
c = list(str(input("문자열을 입력하시오 :")))
start=-1
result = ""
for i in range(len(c)):
    #리스트를 거꾸로 받아서 result 변수에 넣는다.
    result +=c[start-i]

print("반전 문자열 :",result)