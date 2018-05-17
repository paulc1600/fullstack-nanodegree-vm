from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    hw_restaurant = session.query(Restaurant).first()
    print hw_restaurant.id                    # Not printing database values, printing local object attribute? 
    print hw_restaurant.name                  # Not printing database values, printing local object attribute?
	# ------------------------------------------------------- attempt A
    # items = session.query(MenuItem).filter_by(restaurant_id = Restaurant.id) = get ALL menu items???
	# ------------------------------------------------------- attempt B
    # items = session.query(MenuItem).filter_by(restaurant_id = hw_restaurant.id) = breaks 2nd query (this one)
	# 1
	# Pizza Palace
	# SELECT menu_item.name AS menu_item_name, menu_item.id AS menu_item_id, menu_item.course AS menu_item_course, menu_item.description AS menu_item_description, menu_item.price AS menu_item_price, menu_item.restaurant_id AS menu_item_restaurant_id
	# FROM menu_item
	# WHERE menu_item.restaurant_id = ?
    # ------------------------------------------------------- attempt C
    items = session.query(MenuItem).filter_by(restaurant_id = '1') 
	
    print items
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
    print output
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
