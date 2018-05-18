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
# items = session.query(MenuItem).filter_by(restaurant_id = '1') = breaks 2nd query
# Console output same as attempt B
# ------------------------------------------------------- attempt D (fullstack solution)
# items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all() = Creates syntax error
# NameError: global name 'restaurant' is not defined
# ------------------------------------------------------- attempt E (fullstack solution v2)
# items = session.query(MenuItem).filter_by(restaurant_id = r.id).all()
# 1
# Pizza Palace
# []
# 
# - - [17/May/2018 14:24:40] "GET /hello HTTP/1.1" 200 -
# ------------------------------------------------------- attempt F (fullstack solution v3)
# items = session.query(MenuItem).filter_by(restaurant_id = r.id).first() = returns nothing in items
# ------------------------------------------------------- attempt G (fullstack solution v3)
# items = session.query(MenuItem).filter(restaurant_id == r.id).first() = 'restaurant_id' not global name???
	
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
    restaurant = session.query(Restaurant).first()
    rid = ''
    rname = ''
    rid = str(Restaurant.id)
    rname = str(Restaurant.name)
    print "Rest ID = " + rid
    print "Rest Name = " + rname	
	
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    dbg_items = ''
    dbg_items = str(items)
    print "One item = " + dbg_items
    print "Outside the loop ..."
	
    output = ''
    for i in items:
        print "Made it inside the loop ..."   
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)