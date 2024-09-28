import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 요소별 덧셈
sum_array = a + b  # 결과: [5, 7, 9]

# 요소별 곱셈
product_array = a * b  # 결과: [4, 10, 18]

# 행렬 곱셈
matrix_product = np.dot(a, b)  # 결과: 32
