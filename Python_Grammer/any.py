# 여러 조건 중 하나라도 참인지 확인
conditions = [False, False, True, False]
if any(conditions):
    print("조건 중 적어도 하나는 참입니다.")

# 리스트의 요소 중 참인 것이 있는지 확인
numbers = [0, 0, 1, 0]  # 0은 거짓, 1은 참
print(any(numbers))  # True 출력

# 비어있는 리스트는 False 반환
empty_list = []
print(any(empty_list))  # False 출력
