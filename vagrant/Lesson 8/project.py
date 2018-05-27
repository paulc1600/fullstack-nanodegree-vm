from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Return JSON version of menu if requested through this URL
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    qs1 = 'id = ' + str(restaurant_id)
    restaurants = session.query(Restaurant).filter(qs1).one()
    qs2 = 'restaurant_id = ' + str(restaurant_id)
    items = session.query(MenuItem).filter(qs2).all()
    return jsonify(MenuItems=[i.serialize for i in items])

# Return JSON version of single menu item if requested through this URL
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    qs1 = 'id = ' + str(menu_id)
    jsonItem = session.query(MenuItem).filter(qs1).one()
    return jsonify(MenuItems=[i.serialize for i in jsonItem])
	
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    qs1 = 'id = ' + str(restaurant_id)
    restaurants = session.query(Restaurant).filter(qs1).one()
    qs2 = 'restaurant_id = ' + str(restaurant_id)
    items = session.query(MenuItem).filter(qs2).all()
    G_restaurants = restaurants
    G_items = items
    return render_template('menu.html', restaurant=restaurants, items = items)

	
# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/newMenuItem/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        qs1 = 'id = ' + str(restaurant_id)
        restaurants = session.query(Restaurant).filter(qs1).one()
        return render_template('newmenuitem.html', restaurant=restaurants, restaurant_id=restaurant_id)


	
# Create route for editMenuItem function
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/editMenuItem/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    qs1 = 'id = ' + str(menu_id)
    editedItem = session.query(MenuItem).filter(qs1).one()
    qs2 = 'id = ' + str(restaurant_id)
    restaurants = session.query(Restaurant).filter(qs2).one()
	
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            editedItem.description = request.form['description']
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()
        flash("Menu item modified!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem, name=restaurants)


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/deleteMenuItem/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    qs1 = 'id = ' + str(menu_id)
    DelItem = session.query(MenuItem).filter(qs1).one()
	
    if request.method == 'POST':
        session.delete(DelItem)
        session.commit()     
        flash("Menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=DelItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'   # Dev only!!! Normally like password. 
    app.debug = True
    app.run(host='0.0.0.0', port=5000)