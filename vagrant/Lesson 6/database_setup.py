import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Create instance of declarative base
Base = declarative_base()

# Create Tables for Database
class Restaurant(Base):
  __tablename__ = 'restaurant'
  name = Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)

class MenuItem(Base):
  __tablename__ = 'menu_item'
  name = Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)
  course = Column(String(250))
  description = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, Foreign_key('restaurant.id'))
  restaurant = relationship(Restaurant)

### End of File Setting ###
engine = create_engine('sqlite:///restaurantmenu.db')

### Takes classes we'll create and turns them into tables in new database ###
Base.metadata.create_all(engine)
