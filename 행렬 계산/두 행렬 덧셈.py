# 두 행렬의 덧셈을 계산하는 코드를 작성하시오

A =[[1,2], [3,4]]
B =[[4,3], [2,1]]
result =[]

for i in range(2):
    result.append([A[i][0] + B[i][0] ,A[i][1] + B[i][1]])

print(result)