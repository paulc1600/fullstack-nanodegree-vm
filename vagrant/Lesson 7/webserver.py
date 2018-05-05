# encoding=utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import os
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# Set up CRUD Engine session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
message = ""

class WebServerHandler(BaseHTTPRequestHandler):

    ##---------------------------------------------------------------------------##
    ##  Handle WebServer File Requests
    ##---------------------------------------------------------------------------##
    def do_GET(self):
        My_Path = os.getcwd()     # returns a string representing the current working directory
        Req_File = str(self.path)

        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            message += "<form method='POST' enctype='multipart/form-data'  \
                        action='hello'><h2>What would you like me to say?</h2> \
                        <input name='message' type='text'> \
                        <input type='submit' vatue='Submit'></form>"
            self.wfile.write(message)
            print message
            return
        else:   # return ftp page
            if self.path.endswith("/ftp"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message = read_file("easyftp.htm")
                self.wfile.write(message)
                print "easyftp.htm file sent"
                return
            else:  # URL contains no path message / treat as a normal resource request
                os.chdir(My_Path)
                Get_File = Req_File.replace("/", "")
                
                # Special File Preparation Code (if Needed)
                if Get_File is 'restaurant.htm':
                    Get_File_Content = restaurants_htm()
                    write_file(Get_File, Get_File_Content)
                
                # Attempt to get requested file
                try:
                    filep = open(Get_File, "r")
                    file.close(filep)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    message = ""
                    message = read_file(Get_File)
                    self.wfile.write(message)
                    print Get_File + " file sent"
                    return
                except IOError:
                    error1 = "Could not read " + Get_File
                    self.send_error(404, error1)


    ##---------------------------------------------------------------------------##
    ##  Handle Posted Data sent to WebServer
    ##---------------------------------------------------------------------------##
    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += "<h2>OK, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += "<p></p>"
            output += "<form method='POST' enctype='multipart/form-data'  \
                        action='hello'><h2>What would you like me to say?</h2> \
                        <input name='message' type='text'> \
                        <input type='submit' vatue='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

##---------------------------------------------------------------------------##
##  Create HTML for restaurant.htm page (list of restaurants)
##---------------------------------------------------------------------------##
def restaurants_htm():
    restaurant_list = ""
    restaurants_page = '''
<html><body>
<h2>Restaurants List</h2>
<p></p>
{rest_list}
</body></html>
'''
    items = session.query(Restaurant).all()
    for RestRec in items:
        restaurant_list += str(RestRec.name) + " <p></p> "
    Final_HTML = restaurants_page.format(rest_list=restaurant_list)    
    return Final_HTML


##---------------------------------------------------------------------------##
##  I Read Any Text File Given Me (assumes it's there)
##---------------------------------------------------------------------------##        
def read_file(filename):
    file = open(filename, "r")
    my_message = file.read()
    file.close()
    return my_message


##---------------------------------------------------------------------------##
##  I write an input string into a text File named for Me
##---------------------------------------------------------------------------## 
def write_file(filename, filecontent):
    text_file = open(filename, "w")
    text_file.write(filecontent)
    text_file.close()

    
##---------------------------------------------------------------------------##
##  M A I N 
##---------------------------------------------------------------------------##     
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
