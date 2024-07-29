from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Administrator(Base):
    __tablename__ = 'administrators'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    resource_id = Column(Integer)
    ingredient = Column(String)
    amount = Column(DECIMAL)
    unit = Column(String)
