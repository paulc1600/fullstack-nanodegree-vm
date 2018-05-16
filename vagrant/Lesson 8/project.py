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
    filter_id = str(Restaurant.id)
    print filter_id
    print Restaurant.name
    items = session.query(MenuItem).filter_by(restaurant_id = filter_id)
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
