from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    card_info = Column(String)
    transaction_status = Column(String)
    payment_type = Column(String)
