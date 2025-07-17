import copy

# 리스트 안에 리스트가 있는 경우
original = [[1,2],[3,4]]

# 단순 할당
a = original
a[0][0] = 999
print(original)    # [[999, 2], [3, 4]] - 원본 변경됨!

# 얕은 복사
b = original.copy()
b[0][0] = 888
print(original)    # [[888, 2], [3, 4]] - 여전히 원본 변경됨

# 깊은 복사
c = copy.deepcopy(original)
c[0][0] = 777
print(original)    # [[888, 2], [3, 4]] - 원본 객체 유지
print(c)           # [[777, 2], [3, 4]]
