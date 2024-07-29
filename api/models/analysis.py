from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class Analysis(Base):
    __tablename__ = 'analysis'
    id = Column(Integer, primary_key=True)
    sales_data = Column(String)
    customer_data = Column(String)
