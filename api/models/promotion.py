from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True)
    promo_code = Column(String)
    discount = Column(DECIMAL)
    expiry_date = Column(String)
