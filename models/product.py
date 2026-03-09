from sqlalchemy import Column, Integer, String, Float, JSON
from database import Base
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True ,index=True)
    name = Column(String)
    brand = Column(String)
    category = Column(String)
    price = Column(Float)
    specs = Column(JSON)
    socket = Column(String,nullable=True)
    chipset =Column(String,nullable=True)
    form_factor = Column(String,nullable=True)