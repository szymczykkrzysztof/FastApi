from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://deploy_db_ik7p_user:bdFluegY3iBMhgm0aIP0jiHE9fBxeCu3@dpg-crbekprqf0us73dbn2t0-a.frankfurt-postgres.render.com/deploy_db_ik7p'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
