from sqlalchemy import create_engine, ForeignKey, Column, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.mutable import MutableList

Base = declarative_base()


class Company(Base):
    __tablename__ = "companies"
    link = Column("link", String, primary_key=True)
    path = Column(ARRAY(item_type=String))

    def __init__(self, link, path):
        self.link = link
        self.path = path

    def __repr__(self):
        return f"({self.link}) {self.path}"
    
engine = create_engine("postgresql:///companies.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

company = Company("https://hands.ru/", ["company/about/"])
session.add(company)
session.commit()
