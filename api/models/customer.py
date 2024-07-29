from sqlalchemy import Column, Integer
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)