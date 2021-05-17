# 2x2 행렬의 역행렬을 구하는 코드를 작성하되, 역행열이 존재하지 않는 경우를 고려할 수 있도록 코드를 구현하시오.

A =[[1,2], [3,4]]
B =[[4,3], [2,1]]
result =[]

# 만약 ad -bc =0 이면 역행렬은 존재하지 않는다.
invertible =A[0][0] * A[1][1] -A[0][1] * A[1][0]
if invertible == 0:
    print("역행렬이 존재하지 않습니다.")
else:
    result.append([[A[1][1]/invertible, -A[0][1]/invertible], [-A[1][0]/invertible,A[0][0]/invertible]])
    print(result)
