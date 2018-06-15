from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem, RestProperties 

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

# --------------------------------------------------------------------------------(1)
qs1 = 'id = ' + str(1)
RestPropertyRow = session.query(RestProperties).filter(qs1).first()
RestPropertyRow.street="1777 Pike Street"
RestPropertyRow.city="San Diego"
RestPropertyRow.state="CA"
RestPropertyRow.zip="92126"
RestPropertyRow.phone="619-809-0123"
RestPropertyRow.review_rating="3.5"
RestPropertyRow.rest_photo_file="FD1_Restaurant.jpg"
RestPropertyRow.description="All delicious pies made from scratch with their famous hand-rolled dough, and topped off with a wide variety of fresh natural ingredients."   
RestPropertyRow.open_Mon="9:30 AM" 
RestPropertyRow.close_Mon="2:00 PM" 
RestPropertyRow.open_Tue="9:30 AM" 
RestPropertyRow.close_Tue="2:00 PM" 
RestPropertyRow.open_Wed="9:30 AM" 
RestPropertyRow.close_Wed="10:30 PM" 
RestPropertyRow.open_Thu="9:30 AM" 
RestPropertyRow.close_Thu="10:30 PM" 
RestPropertyRow.open_Fri="9:30 AM"
RestPropertyRow.close_Fri="10:30 PM" 
RestPropertyRow.open_Sat="11:00 AM" 
RestPropertyRow.close_Sat="10:30 PM" 
RestPropertyRow.open_Sun="11:00 AM" 
RestPropertyRow.close_Sun="10:30 PM" 
RestPropertyRow.restaurant_id="1"
session.commit()
# --------------------------------------------------------------------------------(2)
qs2 = 'id = ' + str(2)
RestPropertyRow2 = session.query(RestProperties).filter(qs2).first()
RestPropertyRow2.street="2254 Perine Street"
RestPropertyRow2.city="Alexandria"
RestPropertyRow2.state="VA"
RestPropertyRow2.zip="22370"
RestPropertyRow2.phone="703-806-8377"
RestPropertyRow2.review_rating="4.0"
RestPropertyRow2.rest_photo_file="FD2_Restaurant.jpg"
RestPropertyRow2.description="Two all beef patties, lettuce, cheese, pickles, and onions on a sesame seed bun. Special sauce is extra or on the side."
RestPropertyRow2.open_Mon="8:30 AM"
RestPropertyRow2.close_Mon="9:00 PM"
RestPropertyRow2.open_Tue="8:30 AM" 
RestPropertyRow2.close_Tue="9:00 PM" 
RestPropertyRow2.open_Wed="8:30 AM" 
RestPropertyRow2.close_Wed="10:30 PM" 
RestPropertyRow2.open_Thu="8:30 AM"
RestPropertyRow2.close_Thu="10:30 PM"
RestPropertyRow2.open_Fri="8:30 AM"
RestPropertyRow2.close_Fri="10:30 PM"
RestPropertyRow2.open_Sat="11:00 AM"
RestPropertyRow2.close_Sat="10:30 PM" 
RestPropertyRow2.open_Sun="11:00 AM"
RestPropertyRow2.close_Sun="10:30 PM"
RestPropertyRow2.restaurant_id="2"
session.commit()
# --------------------------------------------------------------------------------(3)
qs3 = 'id = ' + str(3)
RestPropertyRow3 = session.query(RestProperties).filter(qs3).first()
RestPropertyRow3.street="547 Patriot Ln"
RestPropertyRow3.city="Richmond"
RestPropertyRow3.state="VA"
RestPropertyRow3.zip="22370"
RestPropertyRow3.phone="703-806-8377"
RestPropertyRow3.review_rating="4.0"
RestPropertyRow3.rest_photo_file="FD2_Restaurant.jpg"
RestPropertyRow3.description="Like an old friend, Richmond's Super Stir Fry has been delighting guests and visitors with it's blend of spicy mandarin cuisine and southern hospitality."
RestPropertyRow3.open_Mon="8:30 AM"
RestPropertyRow3.close_Mon="9:00 PM"
RestPropertyRow3.open_Tue="8:30 AM" 
RestPropertyRow3.close_Tue="9:00 PM" 
RestPropertyRow3.open_Wed="8:30 AM" 
RestPropertyRow3.close_Wed="10:30 PM" 
RestPropertyRow3.open_Thu="8:30 AM"
RestPropertyRow3.close_Thu="10:30 PM"
RestPropertyRow3.open_Fri="8:30 AM"
RestPropertyRow3.close_Fri="10:30 PM"
RestPropertyRow3.open_Sat="11:00 AM"
RestPropertyRow3.close_Sat="10:30 PM" 
RestPropertyRow3.open_Sun="11:00 AM"
RestPropertyRow3.close_Sun="10:30 PM"
RestPropertyRow3.open_Sun="11:00 AM"
RestPropertyRow3.close_Sun="10:30 PM"
RestPropertyRow3.restaurant_id="3"
session.commit()
# --------------------------------------------------------------------------------(4)
qs4 = 'id = ' + str(4)
RestPropertyRow4 = session.query(RestProperties).filter(qs4).first()
RestPropertyRow4.street="909 Yorkshire Circle"
RestPropertyRow4.city="Alexandria"
RestPropertyRow4.state="MN"
RestPropertyRow4.zip="56308"
RestPropertyRow4.phone="252-327-5503"
RestPropertyRow4.review_rating="3.5"
RestPropertyRow4.rest_photo_file="FD3_Restaurant.jpg"
RestPropertyRow4.description="Beautiful garden courtyard dining experience made memorable through a variety of delicious chicken, fish, beef, and vegetable dishes. Rice noodles are a house specialty."
RestPropertyRow4.open_Mon="11:00 AM"
RestPropertyRow4.close_Mon="9:00 PM"
RestPropertyRow4.open_Tue="11:00 AM"
RestPropertyRow4.close_Tue="9:00 PM"
RestPropertyRow4.open_Wed="11:00 AM"
RestPropertyRow4.close_Wed="10:30 PM"
RestPropertyRow4.open_Thu="11:00 AM"
RestPropertyRow4.close_Thu="10:30 PM"
RestPropertyRow4.open_Fri="11:00 AM"
RestPropertyRow4.close_Fri="10:30 PM"
RestPropertyRow4.open_Sat="11:00 AM"
RestPropertyRow4.close_Sat="10:30 PM"
RestPropertyRow4.open_Sun="11:00 AM"
RestPropertyRow4.close_Sun="10:30 PM"
RestPropertyRow4.restaurant_id="4"
session.commit()
# --------------------------------------------------------------------------------(5)
qs5 = 'id = ' + str(5)
RestPropertyRow5 = session.query(RestProperties).filter(qs5).first()
RestPropertyRow5.street="3110 Doctors Drive"
RestPropertyRow5.city="Los Angeles"
RestPropertyRow5.state="CA"
RestPropertyRow5.zip="90017"
RestPropertyRow5.phone="310-341-3892"
RestPropertyRow5.review_rating="4.0"
RestPropertyRow5.rest_photo_file="FD4_Restaurant.jpg"
RestPropertyRow5.description="Perfectly blended and spiced vegetarian and vegan favorites. All made from fresh, organic, locally grown ingredients."
RestPropertyRow5.open_Mon="12:00 PM"
RestPropertyRow5.close_Mon="9:00 PM"
RestPropertyRow5.open_Tue="12:00 PM"
RestPropertyRow5.close_Tue="9:00 PM"
RestPropertyRow5.open_Wed="12:00 PM"
RestPropertyRow5.close_Wed="10:30 PM" 
RestPropertyRow5.open_Thu="12:00 PM"
RestPropertyRow5.close_Thu="10:30 PM"
RestPropertyRow5.open_Fri="12:00 PM"
RestPropertyRow5.close_Fri="10:30 PM"
RestPropertyRow5.open_Sat="12:00 PM"
RestPropertyRow5.close_Sat="10:30 PM"
RestPropertyRow5.open_Sun="Closed"
RestPropertyRow5.close_Sun="Closed"
RestPropertyRow5.restaurant_id="5"
session.commit()
# --------------------------------------------------------------------------------(6)
qs6 = 'id = ' + str(6)
RestPropertyRow6 = session.query(RestProperties).filter(qs6).first()
RestPropertyRow6.street="3079 Joyce Street"
RestPropertyRow6.city="Gulf Shores"
RestPropertyRow6.state="AL"
RestPropertyRow6.zip="36542"
RestPropertyRow6.phone="251-968-2181"
RestPropertyRow6.review_rating="3.0"
RestPropertyRow6.rest_photo_file="FD4_Restaurant.jpg"
RestPropertyRow6.description="Tony himself still greets guests at the door with a hearty handshake. Casual patio dining is available, and all dishes can be complemented with an excellent wine selection." 
RestPropertyRow6.open_Mon="12:00 PM"
RestPropertyRow6.close_Mon="9:00 PM"
RestPropertyRow6.open_Tue="12:00 PM"
RestPropertyRow6.close_Tue="9:00 PM"
RestPropertyRow6.open_Wed="12:00 PM"
RestPropertyRow6.close_Wed="10:30 PM" 
RestPropertyRow6.open_Thu="12:00 PM"
RestPropertyRow6.close_Thu="10:30 PM"
RestPropertyRow6.open_Fri="12:00 PM"
RestPropertyRow6.close_Fri="10:30 PM"
RestPropertyRow6.open_Sat="12:00 PM"
RestPropertyRow6.close_Sat="10:30 PM"
RestPropertyRow6.open_Sun="Closed"
RestPropertyRow6.close_Sun="Closed"
RestPropertyRow6.restaurant_id="6"
session.commit()
# --------------------------------------------------------------------------------(7)
qs7 = 'id = ' + str(7)
RestPropertyRow7 = session.query(RestProperties).filter(qs7).first()
RestPropertyRow7.street="3418 Counts Lane"
RestPropertyRow7.city="West Hartford"
RestPropertyRow7.state="CT"
RestPropertyRow7.zip="06105"
RestPropertyRow7.phone="860-231-3576"
RestPropertyRow7.review_rating="2.0"
RestPropertyRow7.rest_photo_file="FD6_Restaurant.jpg"
RestPropertyRow7.description="Not exactly fine dining, but if you want it fast and cheap, Joe has got it covered. They serve comfort food in large portions, but don't annoy the waitresses."
RestPropertyRow7.open_Mon="4:30 PM"
RestPropertyRow7.close_Mon="10:30 PM"
RestPropertyRow7.open_Tue="4:30 PM"
RestPropertyRow7.close_Tue="10:30 PM"
RestPropertyRow7.open_Wed="4:30 PM"
RestPropertyRow7.close_Wed="10:30 PM"
RestPropertyRow7.open_Thu="4:30 PM"
RestPropertyRow7.close_Thu="10:30 PM"
RestPropertyRow7.open_Fri="4:30 PM"
RestPropertyRow7.close_Fri="10:30 PM"
RestPropertyRow7.open_Sat="12:00 PM"
RestPropertyRow7.close_Sat="10:30 PM"
RestPropertyRow7.open_Sun="Closed"
RestPropertyRow7.close_Sun="Closed"
RestPropertyRow7.restaurant_id="8"
session.commit()
# --------------------------------------------------------------------------------(8)
qs8 = 'id = ' + str(8)
RestPropertyRow8 = session.query(RestProperties).filter(qs8).first()
RestPropertyRow8.street="3155 Sampson Street"
RestPropertyRow8.city="Aurora"
RestPropertyRow8.state="CO"
RestPropertyRow8.zip="80014"
RestPropertyRow8.phone="303-568-6185"
RestPropertyRow8.review_rating="4.0"
RestPropertyRow8.rest_photo_file="FD5_Restaurant.jpg"
RestPropertyRow8.description="Pelican Bay is a secret gem. They serve a wide variety of delicious seafood favorites in a cozy relaxing atmosphere. Friday seafood buffet should not be missed."
RestPropertyRow8.open_Mon="3:00 PM"
RestPropertyRow8.close_Mon="10:30 PM"
RestPropertyRow8.open_Tue="3:00 PM"
RestPropertyRow8.close_Tue="10:30 PM"
RestPropertyRow8.open_Wed="3:00 PM"
RestPropertyRow8.close_Wed="10:30 PM"
RestPropertyRow8.open_Thu="3:00 PM"
RestPropertyRow8.close_Thu="10:30 PM"
RestPropertyRow8.open_Fri="3:00 PM"
RestPropertyRow8.close_Fri="10:30 PM"
RestPropertyRow8.open_Sat="12:00 PM"
RestPropertyRow8.close_Sat="10:30 PM"
RestPropertyRow8.open_Sun="Closed"
RestPropertyRow8.close_Sun="Closed"
RestPropertyRow8.restaurant_id="10"
session.commit()
# --------------------------------------------------------------------------------(9)
qs9 = 'id = ' + str(9)
RestPropertyRow9 = session.query(RestProperties).filter(qs9).first()
RestPropertyRow9.street="2950 Great Oak Trail"
RestPropertyRow9.city="West Hartford"
RestPropertyRow9.state="CT"
RestPropertyRow9.zip="06105"
RestPropertyRow9.phone="860-231-3576"
RestPropertyRow9.review_rating="4.0"
RestPropertyRow9.rest_photo_file="FD6_Restaurant.jpg"
RestPropertyRow9.description="Originally a hunting lodge, House of Gator serves wild and exotic game entrées. It's not for everyone, but you have not lived until you have tried the Beefalo steak." 
RestPropertyRow9.open_Mon="4:30 PM"
RestPropertyRow9.close_Mon="10:30 PM"
RestPropertyRow9.open_Tue="4:30 PM"
RestPropertyRow9.close_Tue="10:30 PM"
RestPropertyRow9.open_Wed="4:30 PM"
RestPropertyRow9.close_Wed="10:30 PM"
RestPropertyRow9.open_Thu="4:30 PM"
RestPropertyRow9.close_Thu="10:30 PM"
RestPropertyRow9.open_Fri="4:30 PM"
RestPropertyRow9.close_Fri="10:30 PM"
RestPropertyRow9.open_Sat="12:00 PM"
RestPropertyRow9.close_Sat="10:30 PM"
RestPropertyRow9.open_Sun="Closed"
RestPropertyRow9.close_Sun="Closed"
RestPropertyRow9.restaurant_id="11"
session.commit()
# --------------------------------------------------------------------------------(10)
qs10 = 'id = ' + str(10)
RestPropertyRow10 = session.query(RestProperties).filter(qs10).first()
RestPropertyRow10.street="3200 Bailey Drive"
RestPropertyRow10.city="Iowa City"
RestPropertyRow10.state="IA"
RestPropertyRow10.zip="52240"
RestPropertyRow10.phone="319-337-8002"
RestPropertyRow10.review_rating="4.0"
RestPropertyRow10.rest_photo_file="FD7_Restaurant.jpg"
RestPropertyRow10.description="Ming has been delighting guests with Mandarin and Cantonese house specialties for many years. Generous portions and sophisticated surroundings round out the experience." 
RestPropertyRow10.open_Mon="5:30 PM"
RestPropertyRow10.close_Mon="10:30 PM"
RestPropertyRow10.open_Tue="5:30 PM"
RestPropertyRow10.close_Tue="10:30 PM"
RestPropertyRow10.open_Wed="5:30 PM"
RestPropertyRow10.close_Wed="10:30 PM"
RestPropertyRow10.open_Thu="5:30 PM"
RestPropertyRow10.close_Thu="10:30 PM"
RestPropertyRow10.open_Fri="5:30 PM"
RestPropertyRow10.close_Fri="10:30 PM"
RestPropertyRow10.open_Sat="12:00 PM"
RestPropertyRow10.close_Sat="10:30 PM" 
RestPropertyRow10.open_Sun="Closed"
RestPropertyRow10.close_Sun="Closed"
RestPropertyRow10.restaurant_id="12"
session.commit()
# --------------------------------------------------------------------------------(11)
qs11 = 'id = ' + str(11)
RestPropertyRow11 = session.query(RestProperties).filter(qs11).first()
RestPropertyRow11.street="3706 Wescam Court"
RestPropertyRow11.city="Fallon"
RestPropertyRow11.state="NV"
RestPropertyRow11.zip="89406"
RestPropertyRow11.phone="775-867-4121"
RestPropertyRow11.review_rating="4.0"
RestPropertyRow11.rest_photo_file="FD8_Restaurant.jpg"
RestPropertyRow11.description="Family style dining in a delightful Italian setting. Pasta dishes must be tried with an appropriate wine from their well-stocked cellar."
RestPropertyRow11.open_Mon="5:30 PM"
RestPropertyRow11.close_Mon="10:30 PM"
RestPropertyRow11.open_Tue="5:30 PM"
RestPropertyRow11.close_Tue="10:30 PM"
RestPropertyRow11.open_Wed="5:30 PM"
RestPropertyRow11.close_Wed="10:30 PM"
RestPropertyRow11.open_Thu="5:30 PM"
RestPropertyRow11.close_Thu="10:30 PM"
RestPropertyRow11.open_Fri="5:30 PM"
RestPropertyRow11.close_Fri="10:30 PM"
RestPropertyRow11.open_Sat="12:00 PM"
RestPropertyRow11.close_Sat="10:30 PM" 
RestPropertyRow11.open_Sun="Closed"
RestPropertyRow11.close_Sun="Closed"
RestPropertyRow11.restaurant_id="13"
session.commit()
# --------------------------------------------------------------------------------
session.close()
print("added restaurant properties!")
