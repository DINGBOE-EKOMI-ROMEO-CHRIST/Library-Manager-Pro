from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(bind = engine)

Base = declarative_base()