from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# ------------------------------------------------------------#
#  (Phase 2) Temp Fake Restaurants -- until database arrives  #
# ------------------------------------------------------------#
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
# ------------------------------------------------------------#
#  (Phase 2) End Temp Code                                    #
# ------------------------------------------------------------#

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# ------------------------------------------------------------#
#  *******    The Gourmet's Friend Index Page    ********     #
#   Template: Main_List.html                                  #
# ------------------------------------------------------------#	
@app.route('/')
@app.route('/restaurant/')
@app.route('/restaurant/list/')
def showRestaurants():
	return render_template('Main_List.html', restaurants=restaurants)

# ------------------------------------------------------------#
#  Create A New Restaurant Record                             #
#   Template: Rest_New.html                                   #
# ------------------------------------------------------------#	
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    return render_template('Rest_New.html')

# ------------------------------------------------------------#
#  Edit A Restaurant Record                                   #
#   Template: Rest_Edit.html                                  #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return render_template('Rest_Edit.html', restaurant_id=restaurant_id, restaurant=restaurant)

# ------------------------------------------------------------#
#  Delete Selected Restaurant Record                          #
#   Template: Rest_Del.html                                   #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
	return render_template('Rest_Del.html', restaurant_id=restaurant_id, restaurant=restaurant)

# ------------------------------------------------------------#
#  Display Selected Restaurant Menu Page                      #
#   Template: Menu_Rest.html                                  #
# ------------------------------------------------------------#		
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    # qs1 = 'id = ' + str(restaurant_id)
    # restaurants = session.query(Restaurant).filter(qs1).one()
    # qs2 = 'restaurant_id = ' + str(restaurant_id)
    # items = session.query(MenuItem).filter(qs2).all()
    # G_restaurants = restaurants
    # G_items = items
    return render_template('Menu_Rest.html', restaurant=restaurant, items = items)

	
# ------------------------------------------------------------#
#  Display Page to Create New Menu Item                       #
#   Template: Menu_Rest_New.html                              #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        # newItem = newMenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        # session.add(newItem)
        # session.commit()
        # flash("New menu item created!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        # qs1 = 'id = ' + str(restaurant_id)
        # restaurants = session.query(Restaurant).filter(qs1).one()
        return render_template('Menu_Rest_New.html', restaurant=restaurant, restaurant_id=restaurant_id)

	
# ------------------------------------------------------------#
#  Display Page to Edit Selected Menu Item                    #
#   Template: Menu_Rest_Edit.html                             #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
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
        # return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
        return 'This page edits menu item ' + str(menu_id) + ' of restaurant ' + str(restaurant_id) + '.'
    else:
        # return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem, name=restaurants)
        return 'This page edits menu item ' + str(menu_id) + ' of restaurant ' + str(restaurant_id) + '.'

		
# ------------------------------------------------------------#
#  Display Page to Delete Selected Menu Item                  #
#   Template: Menu_Rest_Del.html                              #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    qs1 = 'id = ' + str(menu_id)
    DelItem = session.query(MenuItem).filter(qs1).one()
	
    if request.method == 'POST':
        session.delete(DelItem)
        session.commit()     
        flash("Menu item deleted!")
        # return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
        return 'This page deletes menu item ' + str(menu_id) + ' of restaurant ' + str(restaurant_id) + '.'
    else:
        # return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=DelItem)
        return 'This page deletes menu item ' + str(menu_id) + ' of restaurant ' + str(restaurant_id) + '.'


# ------------------------------------------------------------#
#  External API Section                                       #
# ------------------------------------------------------------#
# Return JSON version of menu if requested through this URL
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    qs1 = 'id = ' + str(restaurant_id)
    restaurants = session.query(Restaurant).filter(qs1).one()
    qs2 = 'restaurant_id = ' + str(restaurant_id)
    items = session.query(MenuItem).filter(qs2).all()
    return jsonify(MenuItems=[i.serialize for i in items])

# Return JSON version of single menu item if requested through this URL
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    qs1 = 'id = ' + str(menu_id)
    jsonItem = session.query(MenuItem).filter(qs1).one()
    return jsonify(MenuItems=jsonItem.serialize)		
		
# ------------------------------------------------------------#
#  Main Section                                               #
# ------------------------------------------------------------#		
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'   # Dev only!!! Normally like password. 
    app.debug = True
    app.run(host='0.0.0.0', port=5000)