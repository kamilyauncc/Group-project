from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    dish_name = Column(String)
    ingredients = Column(String)
    price = Column(DECIMAL)
    calories = Column(Integer)
    food_category = Column(String)
    availability = Column(Boolean)
