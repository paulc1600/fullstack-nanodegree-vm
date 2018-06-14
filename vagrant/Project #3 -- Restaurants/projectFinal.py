from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, RestProperties, MenuItem

# ------------------------------------------------------------#
#  (Phase 2) Temp Fake Restaurants -- until database arrives  #
# ------------------------------------------------------------#
#Fake Menu Items for right now
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
    restaurant_rslt = session.query(Restaurant).all()
    properties_rslt = session.query(RestProperties).all()
    
    restaurant_all = []
    nbr_rec_r = 0
    for row in restaurant_rslt:
        # print("  ", row.name)
        rest_rec_dict = {'name' : row.name, 'id' : row.id, 'street' : '', 'city' : '', 'state' : '', 'zip' : '', 'phone' : '', 'description' : '', 
                        'open_Mon' : '', 'close_Mon' : '', 'open_Tue' : '', 'close_Tue' : '', 
                        'open_Wed' : '', 'close_Wed' : '', 'open_Thu' : '', 'close_Thu' : '', 
                        'open_Fri' : '', 'close_Fri' : '', 'open_Sat' : '', 'close_Sat' : '', 
                        'open_Sun' : '', 'close_Sun' : '', 'review_rating' : '', 'rest_photo_file' : '', 'rec_status' : 'Incomplete', 'p_id' : '', 'restaurant_id' : ''}
        restaurant_all.append(rest_rec_dict)
        nbr_rec_r = nbr_rec_r + 1		
		
    properties_all = []
    nbr_rec_p = 0
    for row in properties_rslt:
        # print("  ", row.street)
        prop_rec_dict = {'id' : row.id, 'street' : row.street, 'city' : row.city, 'state' : row.state, 'zip' : row.zip, 'phone' : row.phone, 'description' : row.description, 
                        'open_Mon' : row.open_Mon, 'close_Mon' : row.close_Mon, 'open_Tue' : row.open_Tue, 'close_Tue' : row.close_Tue, 
                        'open_Wed' : row.open_Wed, 'close_Wed' : row.close_Wed, 'open_Thu' : row.open_Thu, 'close_Thu' : row.close_Thu, 
                        'open_Fri' : row.open_Fri, 'close_Fri' : row.close_Fri, 'open_Sat' : row.open_Sat, 'close_Sat' : row.close_Sat, 
                        'open_Sun' : row.open_Sun, 'close_Sun' : row.close_Sun, 'review_rating' : row.review_rating,
                        'rest_photo_file' : row.rest_photo_file, 'restaurant_id' : row.restaurant_id}
        properties_all.append(prop_rec_dict)
        nbr_rec_p = nbr_rec_p + 1

    # Debug broken table links \/\/\/\/\/\/
    for r in range(nbr_rec_r):
        print("All restaurants " + str(restaurant_all[r]['name']) + "\t" + str(restaurant_all[r]['id']) + "\t" + str(restaurant_all[r]['street']) + "\t" + str(restaurant_all[r]['rec_status']) + "\t" + str(restaurant_all[r]['p_id']) + "\t" + str(restaurant_all[r]['restaurant_id'])) 	

    for p in range(nbr_rec_p):
        print("All properties " + str(properties_all[p]['id']) + "\t" + str(properties_all[r]['street']) + "\t" + "\t" + str(properties_all[r]['restaurant_id']))
    # Debug broken table links /\/\/\/\/\/\
		
    # Merge two query results as one big list of dictionary pairs	
    for r in range(nbr_rec_r):
        trg_id = restaurant_all[r]['id']
        for p in range(nbr_rec_p):
            if properties_all[p]['restaurant_id'] == trg_id:
                restaurant_all[r]['street'] = properties_all[p]['street'] 			
                restaurant_all[r]['city'] = properties_all[p]['city']            		
                restaurant_all[r]['state'] = properties_all[p]['state']
                restaurant_all[r]['zip'] = properties_all[p]['zip']
                restaurant_all[r]['phone'] = properties_all[p]['phone']
                restaurant_all[r]['description'] = properties_all[p]['description']
                restaurant_all[r]['open_Mon'] = properties_all[p]['open_Mon']
                restaurant_all[r]['open_Tue'] = properties_all[p]['open_Tue']
                restaurant_all[r]['open_Wed'] = properties_all[p]['open_Wed']
                restaurant_all[r]['open_Thu'] = properties_all[p]['open_Thu']
                restaurant_all[r]['open_Fri'] = properties_all[p]['open_Fri']
                restaurant_all[r]['open_Sat'] = properties_all[p]['open_Sat']
                restaurant_all[r]['open_Sun'] = properties_all[p]['open_Sun']
                restaurant_all[r]['close_Mon'] = properties_all[p]['close_Mon']
                restaurant_all[r]['close_Tue'] = properties_all[p]['close_Tue']
                restaurant_all[r]['close_Wed'] = properties_all[p]['close_Wed']
                restaurant_all[r]['close_Thu'] = properties_all[p]['close_Thu']
                restaurant_all[r]['close_Fri'] = properties_all[p]['close_Fri']
                restaurant_all[r]['close_Sat'] = properties_all[p]['close_Sat']
                restaurant_all[r]['close_Sun'] = properties_all[p]['close_Sun']					
                restaurant_all[r]['review_rating'] = properties_all[p]['review_rating']
                restaurant_all[r]['rest_photo_file'] = properties_all[p]['rest_photo_file']
                restaurant_all[r]['rec_status'] = 'Complete'
                restaurant_all[r]['p_id'] = properties_all[p]['id']
                restaurant_all[r]['restaurant_id'] = properties_all[p]['restaurant_id']

    # Debug broken table links \/\/\/\/\/\/
    for r in range(nbr_rec_r):
        print("All restaurants " + str(restaurant_all[r]['name']) + "\t" + str(restaurant_all[r]['id']) str(restaurant_all[r]['street']) + "\t" + str(restaurant_all[r]['rec_status']) + "\t" + str(restaurant_all[r]['p_id']) + "\t" + str(restaurant_all[r]['restaurant_id'])) 	
    # Debug broken table links /\/\/\/\/\/\
	
    # restaurant_list = session.query(Restaurant, RestProperties).join(RestProperties).filter(RestProperties.restaurant_id == Restaurant.id)	
    return render_template('Main_List.html', restaurants=restaurant_all)

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
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    qs1 = 'id = ' + str(restaurant_id)
    restaurant_2edit = session.query(Restaurant).filter(qs1).one()
    properties_2edit = {'street':'1777 Pike Street','city':'San Diego','state':'CA','zip':'92126','phone':'619-809-0123','review_rating':'3.5','rest_photo_file':'FD1_Restaurant.jpg',
                        'open_Mon':'9:30 AM','close_Mon':'2:00 PM','open_Tue':'9:30 AM','close_Tue':'2:00 PM','open_Wed':'9:30 AM','close_Wed':'10:30 PM',
                        'open_Thu':'9:30 AM','close_Thu':'10:30 PM','open_Fri':'9:30 AM','close_Fri':'10:30 PM','open_Sat':'11:00 AM','close_Sat':'10:30 PM',
                        'open_Sun':'11:00 AM','close_Sun':'10:30 PM'}
    photo_file = str(properties_2edit['rest_photo_file'])
    photo_path2edit = url_for('static', filename = photo_file)
	
    if request.method == 'POST':
        if request.form['name']:
            editedRest.name = request.form['name']
            # editedProperties.street = request.form['street']
            # editedProperties.city = request.form['city']
            # editedProperties.state = request.form['state']
            # editedProperties.zip = request.form['zip']
            # editedProperties.phone = request.form['phone']
            # editedProperties.description = request.form['description']
            # editedProperties.review_rating = request.form['review_rating']
            # editedProperties.rest_photo_file = request.form['rest_photo_file']
            # editedProperties.open_Mon = request.form['open_Mon']
            # editedProperties.close_Mon = request.form['close_Mon']
            # editedProperties.open_Tue = request.form['open_Tue']
            # editedProperties.close_Tue = request.form['close_Tue']
            # editedProperties.open_Wed = request.form['open_Wed']
            # editedProperties.close_Wed = request.form['close_Wed']
            # editedProperties.open_Thu = request.form['open_Thu']
            # editedProperties.close_Thu = request.form['close_Thu']
            # editedProperties.open_Fri = request.form['open_Fri']
            # editedProperties.close_Fri = request.form['close_Fri']
            # editedProperties.open_Sat = request.form['open_Sat']
            # editedProperties.close_Sat = request.form['close_Sat']
            # editedProperties.open_Sun = request.form['open_Sun']
            # editedProperties.close_Sun = request.form['close_Sun']
		
            session.add(editedRest)
            session.commit()
            # session.add(editedProperties)
            # session.commit()		
            flash("Restaurant record modified!")
        else:
            flash("Restaurant record not modified.")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('Rest_Edit.html', restaurant_id=restaurant_id, photo_path = photo_path2edit, 
                                restaurant=restaurant_2edit, properties=properties_2edit)

# ------------------------------------------------------------#
#  Delete Selected Restaurant Record                          #
#   Template: Rest_Del.html                                   #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    qs1 = 'id = ' + str(restaurant_id)
    restaurant_2del = session.query(Restaurant).filter(qs1).one()
    properties_2del = {'street':'1777 Pike Street','city':'San Diego','state':'CA','zip':'92126','phone':'619-809-0123','review_rating':'3.5','rest_photo_file':'FD2_Restaurant.jpg',
                        'open_Mon':'9:30 AM','close_Mon':'2:00 PM','open_Tue':'9:30 AM','close_Tue':'2:00 PM','open_Wed':'9:30 AM','close_Wed':'10:30 PM',
                        'open_Thu':'9:30 AM','close_Thu':'10:30 PM','open_Fri':'9:30 AM','close_Fri':'10:30 PM','open_Sat':'11:00 AM','close_Sat':'10:30 PM',
                        'open_Sun':'11:00 AM','close_Sun':'10:30 PM'}
    photo_file = str(properties_2del['rest_photo_file'])
    photo_path2del = url_for('static', filename = photo_file)
	
    if request.method == 'POST':
        if request.form['name']:
            deletedRest.name = request.form['name']
            # deletedProperties.street = request.form['street']
            # deletedProperties.city = request.form['city']
            # deletedProperties.state = request.form['state']
            # deletedProperties.zip = request.form['zip']
            # deletedProperties.phone = request.form['phone']
            # deletedProperties.description = request.form['description']
            # deletedProperties.review_rating = request.form['review_rating']
            # deletedProperties.rest_photo_file = request.form['rest_photo_file']
            # deletedProperties.open_Mon = request.form['open_Mon']
            # deletedProperties.close_Mon = request.form['close_Mon']
            # deletedProperties.open_Tue = request.form['open_Tue']
            # deletedProperties.close_Tue = request.form['close_Tue']
            # deletedProperties.open_Wed = request.form['open_Wed']
            # deletedProperties.close_Wed = request.form['close_Wed']
            # deletedProperties.open_Thu = request.form['open_Thu']
            # deletedProperties.close_Thu = request.form['close_Thu']
            # deletedProperties.open_Fri = request.form['open_Fri']
            # deletedProperties.close_Fri = request.form['close_Fri']
            # deletedProperties.open_Sat = request.form['open_Sat']
            # deletedProperties.close_Sat = request.form['close_Sat']
            # deletedProperties.open_Sun = request.form['open_Sun']
            # deletedProperties.close_Sun = request.form['close_Sun']
            
            session.delete(deletedRest)
            session.commit()
			# session.delete(deletedProperties)
			# session.commit()			
            flash("Restaurant record deleted!")
        else:
            flash("Restaurant record not deleted.")
        return redirect(url_for('showRestaurants'))
    else:						
        return render_template('Rest_Del.html', restaurant_id=restaurant_id, photo_path = photo_path2del, 
                                restaurant=restaurant_2del, properties=properties_2del)

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
    # qs1 = 'id = ' + str(menu_id)
    # editedItem = session.query(MenuItem).filter(qs1).one()
    # qs2 = 'id = ' + str(restaurant_id)
    # restaurants = session.query(Restaurant).filter(qs2).one()
	
    if request.method == 'POST':
        # if request.form['name']:
        #    editedItem.name = request.form['name']
        #    editedItem.description = request.form['description']
        #    editedItem.price = request.form['price']
        # session.add(editedItem)
        # session.commit()
        # flash("Menu item modified!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('Menu_Rest_Edit.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item, restaurant=restaurant)

		
# ------------------------------------------------------------#
#  Display Page to Delete Selected Menu Item                  #
#   Template: Menu_Rest_Del.html                              #
# ------------------------------------------------------------#	
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # qs1 = 'id = ' + str(menu_id)
    # DelItem = session.query(MenuItem).filter(qs1).one()
	
    if request.method == 'POST':
        # session.delete(DelItem)
        # session.commit()     
        # flash("Menu item deleted!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('Menu_Rest_Del.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item, restaurant=restaurant)


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