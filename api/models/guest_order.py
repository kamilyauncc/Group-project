from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class GuestOrder(Base):
    __tablename__ = 'guest_orders'
    id = Column(Integer, primary_key=True)
    guest_name = Column(String)
    guest_phone = Column(String)
    guest_address = Column(String)
