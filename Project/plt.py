import matplotlib.pyplot as plt

# 데이터 준비
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# bar 차트 생성
plt.bar(categories, values)
plt.title('기본 Bar 차트')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.show()
