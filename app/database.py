import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

name = os.environ.get("DB_NAME")
password = os.environ.get("DB_PASSWORD")
end_point = os.environ.get("DB_URL")
database_name = os.environ.get("DB_NAME_S")

engine = create_engine(f'mysql+pymysql://{name}:{password}@{end_point}/{database_name}')

Session = sessionmaker()
Session.configure(bind=engine)
Base = declarative_base()