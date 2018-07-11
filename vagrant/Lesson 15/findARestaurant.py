from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "00F0LDNICP2MBR1G01ZIUG3HB2BWKV4ZTTLFLIJ4F3KKX2OC"
foursquare_client_secret = "EOGSOCPU4TE0GOFZEGZVRI3PEPKDWUDCM4OCYFV4IKINV40J"

def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude, longitude = getGeocodeLocation(location)
     
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20180711&intent=browse&ll=%s,%s&radius=32200&query=%s&limit=1'% (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    print "URL = %s \n \n" % url
    print "%s response header: %s \n \n" % (location, response)
    venue_record = json.loads(content)
    print "%s response content: %s \n \n" % (location, venue_record)
    venue_id = venue_record['response']['venues'][0]['id']
    venue_name = venue_record['response']['venues'][0]['name']
    venue_address = venue_record['response']['venues'][0]['location']['formattedAddress'][0]
    print "%s Venue ID: %s \n" % (location, venue_id)
    print "%s Venue Name: %s \n" % (location, venue_name)
    print "%s Venue address: %s \n" % (location, venue_address)
	
	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url

	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	# findARestaurant("Tacos", "Jakarta, Indonesia")
	# findARestaurant("Tapas", "Maputo, Mozambique")
	# findARestaurant("Falafel", "Cairo, Egypt")
	# findARestaurant("Spaghetti", "New Delhi, India")
	# findARestaurant("Cappuccino", "Geneva, Switzerland")
	# findARestaurant("Sushi", "Los Angeles, California")
	# findARestaurant("Steak", "La Paz, Bolivia")
	# findARestaurant("Gyros", "Sydney Australia")