import httplib2
import json

def getGeocodeLocation(inputString):
    # Not good idea for production code
    google_api_key = "AIzaSyAAg3DAvm3fLNH4aZFQpIyc18oZxe3uKDQ"
	
	# Replace any blanks with + signs so URL stays valid
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    
    h = httplib2.Http()
    
	# Create actual Google Location request
	#  returns an array with two values
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    # print "response header: %s \n \n" % response
    # print "response content: %s \n \n" % result
    latitude = 0
    longitude = 0
	# print lat and longitude values wanted from JSON data
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    # print "%s Latitude: %s \n" % (inputString, latitude)
    # print "%s Longitude: %s \n \n" % (inputString, longitude)
    return (latitude, longitude)