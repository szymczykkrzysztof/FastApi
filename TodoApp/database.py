from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://tododb_gto0_user:9JisDnSwN3LXwAisZFBXRt29nyjFAuYx@dpg-cs0nut0gph6c73acb200-a.frankfurt-postgres.render.com/tododb_gto0'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
