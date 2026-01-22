from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 엔진 생성
engine = create_engine("postgresql://user:passowr@localhost/dbname")

Session = sessionmaker(bind=engine)

with Session() as session:
  result = session.execute(text("SELECT * FROM users"))
  session.commit()
