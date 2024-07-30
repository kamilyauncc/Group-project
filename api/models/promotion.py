from sqlalchemy import Column, Integer, String, DECIMAL, Date
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True)
    promo_code = Column(String, unique=True)
    discount = Column(DECIMAL)
    expiry_date = Column(Date)
