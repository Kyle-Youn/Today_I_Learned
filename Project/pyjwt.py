'''
pip install pyjwt
'''

import jwt

# 비밀 키와 데이터 설정
secret_key = "my_secret_key"
payload = {"user_id": 123, "role": "admin"}

# JWT 생성
token = jwt.encode(payload, secret_key, algorithm="HS256")
print(f"Encoded JWT: {token}")

# JWT 디코딩
decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
print(f"Decoded JWT: {decoded}")
