from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

engine = create_engine('sqlite:///flaskblog.db',echo=True)
#engine = create_engine(Config.SQLALCHEMY_DATABASE_URI,echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
