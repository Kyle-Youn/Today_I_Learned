import hashlib

def generate_hash(input_string):
    # 입력 문자열을 바이트로 인코딩
    input_bytes = input_string.encode('utf-8')
    
    # SHA-256 해시 객체 생성
    hash_object = hashlib.sha256()
    
    # 데이터 업데이트
    hash_object.update(input_bytes)
    
    # 16진수 문자열로 해시 반환
    return hash_object.hexdigest()

# 사용 예시
if __name__ == "__main__":
    # 사용자로부터 입력 받기
    user_input = input("해시를 생성할 문자열을 입력하세요: ")
    
    # 해시 생성
    hash_result = generate_hash(user_input)
    
    # 결과 출력
    print(f"입력 문자열: {user_input}")
    print(f"SHA-256 해시: {hash_result}")
