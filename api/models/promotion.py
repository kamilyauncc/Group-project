from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True)
    promo_code = Column(String(50))
    discount = Column(DECIMAL)
    expiry_date = Column(String(50))
