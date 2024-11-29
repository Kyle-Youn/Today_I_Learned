import psycopg2

# 데이터베이스 연결 설정
conn = psycopg2.connect(
    host="localhost",     # 데이터베이스 호스트
    database="mydatabase", # 데이터베이스 이름
    user="myuser",         # 데이터베이스 사용자 이름
    password="mypassword"  # 데이터베이스 비밀번호
)

# 커서 생성
cur = conn.cursor()

# SQL 쿼리 실행
cur.execute("SELECT * FROM mytable")

# 데이터 가져오기
rows = cur.fetchall()
for row in rows:
    print(row)

# 커서와 연결 닫기
cur.close()
conn.close()
