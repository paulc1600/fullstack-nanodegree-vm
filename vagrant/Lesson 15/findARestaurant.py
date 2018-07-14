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
    dict_records = {'rest_name': "", 'address': "", 'image': ""}

	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude, longitude = getGeocodeLocation(location)
    
    # -------------------------------------------------------------	
	#  2. Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#      HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	#  3. Grab the first restaurant
	# -------------------------------------------------------------
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20180711&intent=browse&ll=%s,%s&radius=32200&query=%s&limit=1'% (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    # print "URL = %s \n \n" % url
    # print "%s response header: %s \n \n" % (location, response)
    # print "%s response content: %s \n \n" % (location, venue_record)
    venue_record = json.loads(content)
    venue_id = venue_record['response']['venues'][0]['id']
    venue_name = venue_record['response']['venues'][0]['name']
    venue_address = venue_record['response']['venues'][0]['location']['formattedAddress']
    print "%s Venue Latitude: %s" % (location, latitude)
    print "%s Venue Longitude: %s" % (location, longitude)
    print "%s Venue ID: %s" % (location, venue_id)
    print "%s Venue Name: %s" % (location, venue_name)
    print "%s Venue address: %s \n \n" % (location, venue_address)
	
	# ---------------------------------------------------------------------------------
	#  4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#  5. Grab the first image
	#  API DOcs for photos = https://developer.foursquare.com/docs/api/venues/photos
	# ---------------------------------------------------------------------------------
    url_pic = ('https://api.foursquare.com/v2/venues/%s/photos?&client_id=%s&client_secret=%s&v=20180711&limit=1') % (venue_id, foursquare_client_id, foursquare_client_secret)
    rpic_response, rpic_content = h.request(url_pic, 'GET')
    pic_record = json.loads(rpic_content)
    print "%s photo response header: %s \n \n" % (location, rpic_response)
    print "%s photo response content: %s \n \n" % (location, pic_record)
    pic_rcode = pic_record['meta']['code']

    if pic_rcode == 200:
        # To assemble a 4Sq photo URL, combine the response's prefix + size + suffix
        pic_prefix = pic_record['response']['photos']['items'][0]['prefix']
        pic_suffix = pic_record['response']['photos']['items'][0]['suffix']
        pic_width = pic_record['response']['photos']['items'][0]['width']
        pic_height = pic_record['response']['photos']['items'][0]['height']
        pic_URL = pic_prefix + str(pic_width) + 'x' + str(pic_height) + pic_suffix
    else:
	    #6. If no image is available, insert a default image url
        pic_URL = 'default_pic.jpg'	    
	
    print "%s photo URL: %s" % (location, pic_record)
	#7. Return a dictionary containing the restaurant name, address, and image url
    dict_records['rest_name'] = venue_name
    dict_records['address'] = venue_address
    dict_records['image'] = pic_URL
    return dict_records
	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	# findARestaurant("Tacos", "Jakarta, Indonesia")
	# findARestaurant("Tapas", "Maputo, Mozambique")
	# findARestaurant("Falafel", "Cairo, Egypt")
	# findARestaurant("Spaghetti", "New Delhi, India")
	# findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	# findARestaurant("Steak", "La Paz, Bolivia")
	# findARestaurant("Gyros", "Sydney Australia")