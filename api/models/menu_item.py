from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    dish_name = Column(String(51))
    ingredients = Column(String(51))
    price = Column(DECIMAL)
    calories = Column(Integer)
    food_category = Column(String(51))
    availability = Column(Boolean)
