from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# 예시 데이터 생성
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 4])

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
print(model.predict([[5]]))  # 새로운 입력에 대한 예측
