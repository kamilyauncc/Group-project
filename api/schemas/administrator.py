from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Administrator(Base):
    username: str
    password: str
    email: str
    role: str

class Administrator (Base):
   username: Optional[str] = None
   password: Optional[str] = None
   email: Optional[str] = None 
   role: Optional[str] = None


