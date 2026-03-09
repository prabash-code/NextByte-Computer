from sqlalchemy import  Column, Integer, String,Float,JSON,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from database import Base
class stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True,index=True)
    product_id = Column(Integer,ForeignKey('product.id'))
    quantity = Column(Float)

    product=relationship("Product")