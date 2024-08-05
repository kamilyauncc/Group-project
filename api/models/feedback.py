from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    customer_id = Column(Integer)
    review_text = Column(String(50))
    review_score = Column(DECIMAL)
