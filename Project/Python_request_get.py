'''
pip install requests

'''

import requests

# 요청을 보낼 URL
url = "https://www.example.com/data"

response = requests.get(url)

# 응답 코드 체크 (200은 성공)
if response.status_code == 200:
    print("Success!")
    # 응답에서 JSON 데이터를 파싱 (API 응답이 JSON 형식일 경우)
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data.")
    print("Status Code:", response.status_code)
