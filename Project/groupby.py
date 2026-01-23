from itertools import groupby

# 연속된 동일 값 묶기
logs = ["OK", "OK", "ERR", "ERR", "ERR", "OK", "ERR"]
for status, group in groupby(logs):
    if status == "ERR":
        print(f"연속 에러 {len(list(group))}건")
