import hashlib

# SHA-256 해시 생성
data = "Hello world"
hash_object = hashlib.sha256(data.encode())
hex_digest = hash_object.hexdigest()

# 해시 값 출력
