'''
SQLAlchemy(2.0) Core
Workflow sample code
'''
 
# 1) 엔진 생성
from sqlalchemy import create_engine
engine = create_engine('postgresql://admin:1234@10.1.2.55:5432/postgres')
 
 
# 2) 메타데이터(table, schema 정보 내포)
from sqlalchemy import MetaData
metadata = MetaData()
 
 
# 3) 테이블 정의
from sqlalchemy import Table, Column, Integer, String
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)
 
# 4) 테이블 생성
metadata.create_all(engine)
 
 
######################################################
# 5) CRUD
######################################################
# CREATE(INSERT)
from sqlalchemy import select   # select는 함수로 제공되기에 import
with engine.begin() as conn:    # [engine.begin() + with문] 사용 시 자동으로 트랜잭션이 관리됨(편의성 암시적커밋 기능)
    conn.execute(
        users_table.insert(),
        [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    )
 
# (READ)SELECT
with engine.begin() as conn:
    result = conn.execute(select(users_table))
    # .all()로 결과를 리스트로 가져올 수 있음
    rows = result.all()
    print("Initial SELECT:", rows)
 
# UPDATE
with engine.begin() as conn:
    conn.execute(
        users_table.update()
        .where(users_table.c.name == "Bob")
        .values(age=31)
    )
 
# DELETE
with engine.begin() as conn:
    conn.execute(
        users_table.delete()
        .where(users_table.c.name == "Bob")
    )
