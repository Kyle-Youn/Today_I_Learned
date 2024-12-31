'''
SQLAlchemy ORM 예제코드
'''
 
# 엔진 생성
from sqlalchemy import create_engine
DATABASE_URL = 'postgresql://admin:1234@localhost:5432/'
engine = create_engine(DATABASE_URL, echo=True)
 
 
# Base 준비(schema 정보)
from sqlalchemy.orm import declarative_base
Base = declarative_base()
 
 
# 테이블 정의
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
 
# 테이블 생성
Base.metadata.create_all(engine)    # 테이블 생성
 
# Session 팩토리 생성
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(engine)
 
'''
CRUD
'''
 
# INSERT
with SessionLocal() as session:
    new_user = User(username="june", email="june@gmail.com")
    session.add(new_user)
    session.commit()
 
# SELECT
with SessionLocal() as session:
    user = session.query(User).filter(User.username == "june").first()
    if user:
        print(user.id, user.username, user.email)
    else:
        print("User not found.")
