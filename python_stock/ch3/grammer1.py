import numpy as np

A = np.array([[1,2], [3,4]])

# 배열 정보보기.
print("배열 정보보기")
print(A)
print(type(A))
print(A.ndim)
print(A.shape)


print(A[0], A[1])
print(A.max(), A.min(), A.mean(), A.sum())
print("#################")

# 배열의 접근
print("배열의 접근")
print(A[0], A[1])
print(A[A>1]) # A배열의 원소 중 1보다 큰 것만 출력.


# 배열의 형태 바꾸기.
print("배열의 형태 바꾸기")
print(A)
print(A.flatten())

# 배열의 연산.
print("배열의 연산")
print(A+A)
print(A - A)
print(A * A)
print(A / A)



# 브로드 캐스팅
print("브로드 캐스팅")
B = np.array([10, 100])
print(B)
print(A * B)

# 내적구하기
print("내적 구하기")
B.dot(B)
print(B.dot(B))

A.dot(B)
print(A.dot(B))