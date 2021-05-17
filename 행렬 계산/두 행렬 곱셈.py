# 두 행렬의 곱셈을 계산하는 코드를 작성하시오

A =[[1,2], [3,4]]
B =[[4,3], [2,1]]
result =[]

for i in range(2):
    result.append([A[i][0] * B[0][0] +A[i][1] * B[1][0] ,A[i][0] * B[0][1] + A[i][1] * B[1][1]])

print(result)
