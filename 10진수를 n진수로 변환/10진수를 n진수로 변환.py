n = int(input("10진수를 입력하시오 :"))
m = int(input("바꿀 진법수를 입력하시오 :"))
result = ""
while (n>0):
    remainder = n%m
    n =n//m
    result = str(remainder)+result
print("바꾼 진법수:",result)