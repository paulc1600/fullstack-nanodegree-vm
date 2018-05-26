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
  restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
  restaurant = relationship(Restaurant)

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
  
### End of File Setting ###
engine = create_engine('sqlite:///restaurantmenu.db')


### Takes classes we'll create and turns them into tables in new database ###
Base.metadata.create_all(engine)
