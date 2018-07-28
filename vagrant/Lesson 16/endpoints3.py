from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Puppy

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) 

# Create the appropriate app.route functions, 
# test and see if they work

#Make an app.route() decorator here
@app.route('/')
def puppyControl():
	return render_template('puppycontrol.html')

	
#Make an app.route() decorator here
@app.route('/puppies/', methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
  	    #Call the method to Get all of the puppies
        return getAllPuppies()
  
    elif request.method == 'POST':
  	    #Call the method to make a new puppy
        print "Making a New puppy"
    
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        print name
        print description
        return makeANewPuppy(name, description)

	
#Make another app.route() decorator here that takes in an integer id in the 
@app.route('/puppies/<int:id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
#Call the method to view a specific puppy
def puppiesFunctionId(id):
    if request.method == 'GET':
        return getPuppy(id)

    #Call the method to edit or remove a specific puppy (works with browser / template)  
    elif request.method == 'POST':
        value = request.args.get('value', '')
        if value == 'PUT':
            name = request.args.get('name', '')
            description = request.args.get('description', '')
            return updatePuppy(id,name, description)
        elif value == 'DELETE':
            return deletePuppy(id)	
    
    #Call the method to edit a specific puppy (can never do from browser) 
    elif request.method == 'PUT':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        return updatePuppy(id,name, description)
    
    #Call the method to remove a puppy (can never do from browser)
    elif request.method == 'DELETE':
        return deletePuppy(id)


def getAllPuppies():
    puppies = session.query(Puppy).all()
    return jsonify(Puppies=[i.serialize for i in puppies])
  
def makeANewPuppy(name, description):
    puppy = Puppy(name = name, description = description)
    session.add(puppy)
    session.commit()
    return jsonify(Puppy=puppy.serialize)

def getPuppy(id):
    puppy = session.query(Puppy).filter_by(id = id).one()
    return jsonify(puppy=puppy.serialize) 
	
def updatePuppy(id):
    puppy = session.query(Puppy).filter_by(id = id).one()
    if not name:
        puppy.name = name
    if not description:
        puppy.description = description

    session.add(puppy)
    session.commit()
    return "Updated a Puppy with id %s" % id

def deletePuppy(id):
    puppy = session.query(Puppy).filter_by(id = id).one()
    session.delete(puppy)
    session.commit()
    return "Removed Puppy with id %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	  
