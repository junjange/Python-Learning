# 사칙연산을 수행하는 계산기 함수를 구현

def calculator(x, y, z):
    if z == '+':
        return x+y
    elif z == '-':
        return x-y
    elif z == '*':
        return x*y
    elif z == '/':
        return x/y
    else:
        print("연산자를 다시 입력해주세요.")
        
result = calculator(1,5,'*')
print(result)