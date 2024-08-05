from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    card_info = Column(String(51))
    transaction_status = Column(String(51))
    payment_type = Column(String(51))

    order = relationship("Order", back_populates="payment")
