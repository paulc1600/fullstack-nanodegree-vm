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
        os.chdir(My_Path)
        Get_File = Req_File.replace("/", "")
        GFT1 = Get_File[-4:]
        GFT2 = Get_File[-5:]
        Get_File_Content = ""
        
        # Internal resources (server creates resources)
        if GFT1 != '.htm' and GFT2 != '.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if Get_File == 'restaurants':
                Get_File_Content = restaurants_htm()
            else:
                if Get_File == 'rest_new':
                    Get_File_Content = rest_new_htm()    
                else:
                    if Get_File == 'hello':
                        Get_File_Content = hello_htm()
                    
            # Send message first
            self.wfile.write(Get_File_Content)
            print Get_File_Content
            
            # Create Cache Copy / Debug, etc.
            Get_File += '.htm'
            write_file(Get_File, Get_File_Content)
            return   
        else:  # URL contains no path message / not internal resource / treat as simple file request
            os.chdir(My_Path)
            
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
<html>
<head><link rel="icon" href="data:,"></head>
<body>
<h3><a href="rest_new">Create New Restaurant</a></h3>
<p></p>
<h2>Restaurants List</h2>
<p></p>
<table style="width:100%" border=0>
  <tr>
    <th>Restaurant Name</th>
    <th></th> 
    <th></th>
  </tr>
{rest_list}
</table>
</body></html>
'''
    items = session.query(Restaurant).all()
    for RestRec in items:
        restaurant_list += "<tr>"
        restaurant_list += "<td> " + str(RestRec.name) + "</td>"
        restaurant_list += '''<td><a href="Rest_Edit.htm">Edit</a></td>'''
        restaurant_list += '''<td><a href="Rest_Delete.htm">Delete</a></td>'''
        restaurant_list += "</tr>"
    Final_HTML = restaurants_page.format(rest_list=restaurant_list)    
    return Final_HTML


##---------------------------------------------------------------------------##
##  Create HTML for new restaurant code
##---------------------------------------------------------------------------##
def rest_new_htm():
    new_page = ""
    new_page += "<html>"
    new_page += '''<head><link rel="icon" href="data:,"></head>'''
    new_page += "<body>"
    new_page += "<h2>Make A New Restaurant"</h2>"
    new_page += "<p></p>"
    new_page += "<form method='POST' enctype='multipart/form-data' action='new'> \
                    <input name='message' type='text'> \
                    <input type='submit' vatue='Create'></form>" 
    new_page += "</body></html>"
    return new_page


##---------------------------------------------------------------------------##
##  Create HTML for hello code
##---------------------------------------------------------------------------##
def hello_htm():
    hello_page = ""
    hello_page += "<html>"
    hello_page += '''<head><link rel="icon" href="data:,"></head>'''
    hello_page += "<body>Hello!"
    hello_page += "<p></p>"
    hello_page += "<form method='POST' enctype='multipart/form-data'  \
                    action='hello'><h2>What would you like me to say?</h2> \
                    <input name='message' type='text'> \
                    <input type='submit' vatue='Submit'></form>" 
    hello_page += "</body></html>"
    return hello_page


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
    return

    
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
