import sys
from sqlalchemy import Column, Foreignkey, Integer, String
from sqlalchemy.ext.declarative import declarative base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Create instance of declarative base
Base = declarative_base()

# Create Tables for Database
class Restaurant(Base):


class MenuItem(Base):




### End of File Setting ###
engine = create_engine('sqlite:///restaurantmenu.db')

### Takes classes we'll create and turns them into tables in new database ###
Base.metadata.create_all(engine)
