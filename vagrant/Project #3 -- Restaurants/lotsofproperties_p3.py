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

# --------------------------------------------------------------------------------
qs1 = "name = " + str('Pizza Palace')
print(qs1)
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="1777 Pike Street", city="San Diego", state="CA", zip="92126", phone="619-809-0123", review_rating="3.5", rest_photo_file="FD1_Restaurant.jpg",
                               description="All delicious pies made from scratch with their famous hand-rolled dough, and topped off with a wide variety of fresh natural ingredients.",   
                               open_Mon="9:30 AM", close_Mon="2:00 PM", open_Tue="9:30 AM", close_Tue="2:00 PM", open_Wed="9:30 AM", close_Wed="10:30 PM", 
                               open_Thu="9:30 AM", close_Thu="10:30 PM", open_Fri="9:30 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Urban Burger') 
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty2 = RestProperties(street="2254 Perine Street", city="Alexandria", state="VA", zip="22370", phone="703-806-8377", review_rating="4.0", rest_photo_file="FD2_Restaurant.jpg",
                               description="Two all beef patties, lettuce, cheese, pickles, and onions on a sesame seed bun. Special sauce is extra or on the side.", 
                               open_Mon="8:30 AM", close_Mon="9:00 PM", open_Tue="8:30 AM", close_Tue="9:00 PM", open_Wed="8:30 AM", close_Wed="10:30 PM", 
                               open_Thu="8:30 AM", close_Thu="10:30 PM", open_Fri="8:30 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Super Stir Fry')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty2 = RestProperties(street="2254 Perine Street", city="Alexandria", state="VA", zip="22370", phone="703-806-8377", review_rating="4.0", rest_photo_file="FD2_Restaurant.jpg",
                               description="Like an old friend, Alexandria's Super Stir Fry has been delighting guests and visitors with it's blend of spicy mandarin cuisine and southern hospitality.", 
                               open_Mon="8:30 AM", close_Mon="9:00 PM", open_Tue="8:30 AM", close_Tue="9:00 PM", open_Wed="8:30 AM", close_Wed="10:30 PM", 
                               open_Thu="8:30 AM", close_Thu="10:30 PM", open_Fri="8:30 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Panda Garden')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="909 Yorkshire Circle", city="Alexandria", state="MN", zip="56308", phone="252-327-5503", review_rating="3.5", rest_photo_file="FD3_Restaurant.jpg",
                               description="Beautiful garden courtyard dining experience made memorable through a variety of delicious chicken, fish, beef, and vegetable dishes. Rice noodles are a house specialty.", 
                               open_Mon="11:00 AM", close_Mon="9:00 PM", open_Tue="11:00 AM", close_Tue="9:00 PM", open_Wed="11:00 AM", close_Wed="10:30 PM", 
                               open_Thu="11:00 AM", close_Thu="10:30 PM", open_Fri="11:00 AM", close_Fri="10:30 PM", open_Sat="11:00 AM", close_Sat="10:30 PM", 
                               open_Sun="11:00 AM", close_Sun="10:30 PM", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Thyme for That Vegetarian Cuisine')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty2 = RestProperties(street="3110 Doctors Drive", city="Los Angeles", state="CA", zip="90017", phone="310-341-3892", review_rating="4.0", rest_photo_file="FD4_Restaurant.jpg",
                               description="Perfectly blended and spiced vegetarian and vegan favorites. All made from fresh, organic, locally grown ingredients.", 
                               open_Mon="12:00 PM", close_Mon="9:00 PM", open_Tue="12:00 PM", close_Tue="9:00 PM", open_Wed="12:00 PM", close_Wed="10:30 PM", 
                               open_Thu="12:00 PM", close_Thu="10:30 PM", open_Fri="12:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Tony\'s Bistro')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="3079 Joyce Street", city="Gulf Shores", state="AL", zip="36542", phone="251-968-2181", review_rating="3.0", rest_photo_file="FD4_Restaurant.jpg",
                               description="Tony himself still greets guests at the door with a hearty handshake. Casual patio dining is available, and all dishes can be complemented with an excellent wine selection.", 
                               open_Mon="12:00 PM", close_Mon="9:00 PM", open_Tue="12:00 PM", close_Tue="9:00 PM", open_Wed="12:00 PM", close_Wed="10:30 PM", 
                               open_Thu="12:00 PM", close_Thu="10:30 PM", open_Fri="12:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Uncle Joe\'s Diner')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="3418 Counts Lane", city="West Hartford", state="CT", zip="06105", phone="860-231-3576", review_rating="2.0", rest_photo_file="FD6_Restaurant.jpg",
                               description="Not exactly fine dining, but if you want it fast and cheap, Joe has got it covered. They serve comfort food in large portions, but don't annoy the waitresses.", 
                               open_Mon="4:30 PM", close_Mon="10:30 PM", open_Tue="4:30 PM", close_Tue="10:30 PM", open_Wed="4:30 PM", close_Wed="10:30 PM", 
                               open_Thu="4:30 PM", close_Thu="10:30 PM", open_Fri="4:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Pelican Bay Oyster House')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty2 = RestProperties(street="3155 Sampson Street", city="Aurora", state="CO", zip="80014", phone="303-568-6185", review_rating="4.0", rest_photo_file="FD5_Restaurant.jpg",
                               description="Pelican Bay is a secret gem. They serve a wide variety of delicious seafood favorites in a cozy relaxing atmosphere. Friday seafood buffet should not be missed.",  
                               open_Mon="3:00 PM", close_Mon="10:30 PM", open_Tue="3:00 PM", close_Tue="10:30 PM", open_Wed="3:00 PM", close_Wed="10:30 PM", 
                               open_Thu="3:00 PM", close_Thu="10:30 PM", open_Fri="3:00 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Bill\'s House of Gator')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="3418 Counts Lane", city="West Hartford", state="CT", zip="06105", phone="860-231-3576", review_rating="4.0", rest_photo_file="FD6_Restaurant.jpg",
                               description="Originally a hunting lodge, House of Gator serves wild and exotic game entrées. It's not for everyone, but you have not lived until you have tried the Beefalo steak.", 
                               open_Mon="4:30 PM", close_Mon="10:30 PM", open_Tue="4:30 PM", close_Tue="10:30 PM", open_Wed="4:30 PM", close_Wed="10:30 PM", 
                               open_Thu="4:30 PM", close_Thu="10:30 PM", open_Fri="4:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Ming Wang Wok Palace')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty2 = RestProperties(street="3200 Bailey Drive", city="Iowa City", state="IA", zip="52240", phone="319-337-8002", review_rating="4.0", rest_photo_file="FD7_Restaurant.jpg",
                               description="Ming has been delighting guests with Mandarin and Cantonese house specialties for many years. Generous portions and sophisticated surroundings round out the experience.", 
                               open_Mon="5:30 PM", close_Mon="10:30 PM", open_Tue="5:30 PM", close_Tue="10:30 PM", open_Wed="5:30 PM", close_Wed="10:30 PM", 
                               open_Thu="5:30 PM", close_Thu="10:30 PM", open_Fri="5:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty2)
session.commit()


# --------------------------------------------------------------------------------
qs1 = "name = " + str('Boca Do Papa')
restaurant1 = session.query(Restaurant).filter(qs1).first()
RestProperty1 = RestProperties(street="3706 Wescam Court", city="Fallon", state="NV", zip="89406", phone="775-867-4121", review_rating="4.0", rest_photo_file="FD8_Restaurant.jpg",
                               description="Family style dining in a delightful Italian setting. Pasta dishes must be tried with an appropriate wine from their well-stocked cellar.", 
                               open_Mon="5:30 PM", close_Mon="10:30 PM", open_Tue="5:30 PM", close_Tue="10:30 PM", open_Wed="5:30 PM", close_Wed="10:30 PM", 
                               open_Thu="5:30 PM", close_Thu="10:30 PM", open_Fri="5:30 PM", close_Fri="10:30 PM", open_Sat="12:00 PM", close_Sat="10:30 PM", 
                               open_Sun="Closed", close_Sun="Closed", restaurant=restaurant1)
session.add(RestProperty1)
session.commit()


print("added restaurant properties!")
