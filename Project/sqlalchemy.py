from sqlalchemy import create_engine, Date, LargeBinary
from sqlalchemy.orm import declarative_base, Session

# Create database engine
from sqlalchemy import create_engine
DATABASE_URL = 'postgresql://admin:1234@localhost:5432/'
engine = create_engine(DATABASE_URL, echo=True)
 
 
# Declarative_base
from sqlalchemy.orm import declarative_base
Base = declarative_base()
 
 
# Define table
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String(50)), nullable=False)
    email = Column(String(100), nullable=False)
 
 
# Create table & session
from sqlalchemy.orm import sessionmaker
Base.metadata.create_all(engine)    # Make table in Database
SessionLocal = sessionmaker(bind=engine)    # Make sessionmaker
session = SessionLocal()    # Make session object
 
 
'''
CRUD
'''
# INSERT
new_user = User(username="june", email="june@gmail.com")
session.add(new_user)
session.commit()
 
 
# SELECT
user = session.query(User).filter(User.username == "alice").first()
print(user.id, user.username, user.email)
