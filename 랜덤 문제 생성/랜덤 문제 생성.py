# 랜덤하게 문제가 나오게 하기 위해서 랜덤 모듈을 사용한다.
import random

# 5개의 문제를 리스트 형식으로 만든다.
a_problem = [2, 4, 6, 8]
b_problem = [1, 3, 5, 7]
c_problem = [13, 16, 19, 22]
d_problem = [100, 200, 300, 400]
e_problem = [1, 4, 9, 16]

# 5개의 문제를 하나의 workbook에 리스트 형식으로 넣는다.
workbook = [a_problem, b_problem, c_problem, d_problem, e_problem]

# 정답 갯수
cnt = 0

# workbook에 문제가 사라질때까지 반복한다.
while workbook:
    
    # 문제를 랜덤하게 제출한다.
    problem = random.choice(workbook)
    result = int(input("{0} {1} {2} 다음수는 무엇일까요? ".format(problem[0], problem[1], problem[2])))
    if result == problem[3]:
        print("정답입니다.")
        # 정답이면 카운터를 해준다.
        cnt +=1
    else:
        print("틀렸습니다.")
        
    # 제출한 문제는 workbook에서 제거한다.
    workbook.remove(problem)

print("5문제중에 {0}문제 정답입니다.".format(cnt))