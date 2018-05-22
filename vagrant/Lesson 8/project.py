from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

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
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        qs1 = 'id = ' + str(restaurant_id)
        restaurants = session.query(Restaurant).filter(qs1).one()
        return render_template('newmenuitem.html', restaurant=restaurants, restaurant_id=restaurant_id)


	
# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/editMenuItem/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/deleteMenuItem/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)