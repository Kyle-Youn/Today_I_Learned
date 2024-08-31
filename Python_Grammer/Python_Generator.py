def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)    # 변수에 generator객체 할당
print(counter)    # <generator object count_up_to at 0x...> 출력

counter = count_up_to(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5
