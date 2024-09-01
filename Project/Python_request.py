'''
Requests : HTTP 요청을 쉽게 보낼 수 있게 해주는 라이브러리
    - 다양한 HTTP 메소드 지원 (GET, POST, PUT, DELETE 등)
'''

import requests

response = requests.get('https://www.naver.com')
print(response.status_code)  # 상태 코드 출력
print(response.text)  # 응답 내용 출력
