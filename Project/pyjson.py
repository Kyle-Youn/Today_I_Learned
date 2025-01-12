import json

# 파이썬 딕셔너리
data = {
  "name": "John",
  "age": 30
}

# 딕셔너리를 JSON 문자열로 변환
json_data = json.dumps(data)
print(json_data)
