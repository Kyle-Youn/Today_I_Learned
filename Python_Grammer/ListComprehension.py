# 기존의 for 루프를 사용한 리스트 생성
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 리스트 컴프리헨션을 사용한 리스트 생성
squares = [x**2 for x in range(10)]
print(squares)  # 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
