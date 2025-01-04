from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, text
from sqlalchemy.exc import SQLAlchemyError
from concurrent.futures import ThreadPoolExecutor
import time
import psycopg2

# 엔진 생성
engine = create_engine(
    'postgresql://admin:1234@10.1.2.55:5432/postgres',
    pool_size=1,
    max_overflow=1
)

# 메타데이터
metadata = MetaData()

# 테이블 정의
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)

# 테이블 생성
metadata.create_all(engine)

# 병렬 작업 수행 함수 정의
def perform_database_operations():
    try:
        with engine.begin() as conn:
            # INSERT
            conn.execute(
                users_table.insert(),
                [{"name": "Alice"}, {"name": "Bob"}]
            )
            # SELECT
            result = conn.execute(select(users_table))
            rows = result.all()
            print("Selected rows:", rows)
    except (SQLAlchemyError, psycopg2.OperationalError) as e:
        print("Error occurred:", e)
        print("Attempting to reconnect...")
        time.sleep(5)  # 재시도 전 대기 시간
        perform_database_operations()

# 병렬로 여러 작업 실행
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(perform_database_operations) for _ in range(20)]
