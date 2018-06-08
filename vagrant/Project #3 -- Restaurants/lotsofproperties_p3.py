from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

qs1 = 'name = ' + str("Urban Burger")
restaurant1 = session.query(Restaurant).filter(qs1)
RestProperty1 = RestProperties(street="1777 Pike Street", city="San Diego", state="CA", zip="92126", phone="619-809-0123", review_rating="3.5", rest_photo_file="FD1_Restaurant.jpg", 
                               open_Mon="9:30 AM", close_Mon="2:00 PM", open_Tue="9:30 AM", close_Tue="2:00 PM", open_Wed="9:30 AM", close_Wed="10:30 PM", 
                               open_Thu="9:30 AM", close_Thu="10:30 PM", open_Fri="9:30 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


qs1 = 'name = ' + str("Super Stir Fry")
restaurant1 = session.query(Restaurant).filter(qs1)
RestProperty2 = RestProperties(street="2254 Perine Street", city="Alexandria", state="VA", zip="22370", phone="703-806-8377", review_rating="4.0", rest_photo_file="FD2_Restaurant.jpg", 
                               open_Mon="8:30 AM", close_Mon="9:00 PM", open_Tue="8:30 AM", close_Tue="9:00 PM", open_Wed="8:30 AM", close_Wed="10:30 PM", 
                               open_Thu="8:30 AM", close_Thu="10:30 PM", open_Fri="8:30 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


qs1 = 'name = "Panda Garden"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty1 = RestProperties(street="909 Yorkshire Circle", city="Alexandria", state="MN", zip="56308", phone="252-327-5503", review_rating="3.5", rest_photo_file="FD3_Restaurant.jpg", 
                               open_Mon="11:00 AM", close_Mon="9:00 PM", open_Tue="11:00 AM", close_Tue="9:00 PM", open_Wed="11:00 AM", close_Wed="10:30 PM", 
                               open_Thu="11:00 AM", close_Thu="10:30 PM", open_Fri="11:00 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()

qs1 = 'name = "Thyme for That Vegetarian Cuisine"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty2 = RestProperties(street="3110 Doctors Drive", city="Los Angeles", state="CA", zip="90017", phone="310-341-3892", review_rating="4.0", rest_photo_file="FD4_Restaurant.jpg", 
                               open_Mon="12:00 PM", close_Mon="9:00 PM", open_Tue="12:00 PM", close_Tue="9:00 PM", open_Wed="12:00 PM", close_Wed="10:30 PM", 
                               open_Thu="12:00 PM", close_Thu="10:30 PM", open_Fri="12:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


qs1 = 'name = "Tony\'s Bistro"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty1 = RestProperties(street="3079 Joyce Street", city="Gulf Shores", state="AL", zip="36542", phone="251-968-2181", review_rating="3.0", rest_photo_file="FD4_Restaurant.jpg", 
                               open_Mon="12:00 PM", close_Mon="9:00 PM", open_Tue="12:00 PM", close_Tue="9:00 PM", open_Wed="12:00 PM", close_Wed="10:30 PM", 
                               open_Thu="12:00 PM", close_Thu="10:30 PM", open_Fri="12:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


qs1 = 'name = "Andala\'s"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty2 = RestProperties(street="3155 Sampson Street", city="Aurora", state="CO", zip="80014", phone="303-568-6185", review_rating="4.0", rest_photo_file="FD5_Restaurant.jpg", 
                               open_Mon="3:00 PM", close_Mon="10:30 PM", open_Tue="3:00 PM", close_Tue="10:30 PM", open_Wed="3:00 PM", close_Wed="10:30 PM", 
                               open_Thu="3:00 PM", close_Thu="10:30 PM", open_Fri="3:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


qs1 = 'name = "Auntie Ann\'s Diner"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty1 = RestProperties(street="3418 Counts Lane", city="West Hartford", state="CT", zip="06105", phone="860-231-3576", review_rating="4.0", rest_photo_file="FD6_Restaurant.jpg", 
                               open_Mon="4:30 PM", close_Mon="10:30 PM", open_Tue="4:30 PM", close_Tue="10:30 PM", open_Wed="4:30 PM", close_Wed="10:30 PM", 
                               open_Thu="4:30 PM", close_Thu="10:30 PM", open_Fri="4:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


qs1 = 'name = "Cocina Y Amor"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty2 = RestProperties(street="3200 Bailey Drive", city="Iowa City", state="IA", zip="52240", phone="319-337-8002", review_rating="4.0", rest_photo_file="FD7_Restaurant.jpg", 
                               open_Mon="5:30 PM", close_Mon="10:30 PM", open_Tue="5:30 PM", close_Tue="10:30 PM", open_Wed="5:30 PM", close_Wed="10:30 PM", 
                               open_Thu="5:30 PM", close_Thu="10:30 PM", open_Fri="5:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()

qs1 = 'name = "State Bird Provisions"'
restaurant1 = session.query(Restaurant).filter(qs1).one()
RestProperty1 = RestProperties(street="3706 Wescam Court", city="Fallon", state="NV", zip="89406", phone="775-867-4121", review_rating="4.0", rest_photo_file="FD8_Restaurant.jpg", 
                               open_Mon="5:30 PM", close_Mon="10:30 PM", open_Tue="5:30 PM", close_Tue="10:30 PM", open_Wed="5:30 PM", close_Wed="10:30 PM", 
                               open_Thu="5:30 PM", close_Thu="10:30 PM", open_Fri="5:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


print("added restaurant properties!")
