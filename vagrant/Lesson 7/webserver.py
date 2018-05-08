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
            if Get_File == 'restaurants' or Get_File == 'index':
                Get_File_Content = restaurants_htm()
            else:
                if Get_File == 'rest_new':
                    Get_File_Content = rest_new_htm()    
                else:
                    if Get_File == 'hello':
                        Get_File_Content = hello_htm()
                    else:
                        Get_File_Content = unrec_get(Get_File)
                    
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
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        if ctype == 'multipart/form-data':
            self.send_response(301)
            self.end_headers()
        
            fields=cgi.parse_multipart(self.rfile, pdict)
            # Don't know why had to force brackets off these strings ???
            messagecontent = str(fields.get('message')).replace("[", "")
            messagecontent = messagecontent.replace("]", "")
            Form_Label = str(fields.get('label')).replace("[", "")
            Form_Label = Form_Label.replace("]", "")            
            print '1 ' + messagecontent
            print '1 ' + Form_Label

            # Depending on which form posted back, create response  
            
            # if str(Form_Label) == "rest_new":
            if self.path.endswith("newr_post"):
                # new Restaurant Name updates database
                myNewRestaurant = Restaurant(name = str(messagecontent))
                session.add(myNewRestaurant)
                session.commit()
    
                # Back to restaurant list
                output_msg = newr_post_type(messagecontent, Form_Label)
                self.wfile.write(output_msg)
                return
            else:
                print 'Not rest_new ' + Form_Label
                # if str(Form_Label) == "hello":
                if self.path.endswith("hello"):
                    output_msg = hello_post_type(messagecontent, Form_Label)
                    self.wfile.write(output_msg)
                    return
                else:
                    print 'Not hello ' + Form_Label    
                    output_msg = unrec_post_type(ctype, messagecontent, Form_Label)
                    self.wfile.write(output_msg)
                    return
        else:        
            # No Idea What Posted    
            output_msg = ifmt_post_type(ctype, messagecontent, Form_Label)
            self.wfile.write(output_msg)
            return
        
        
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
<p></p>
<h3><a href="hello">Play Hello Game</a></h3>
</body></html>
'''
    items = session.query(Restaurant).all()
    for RestRec in items:
        restaurant_list += "<tr>"
        restaurant_list += "<td> " + str(RestRec.name) + "</td>"
        restaurant_list += '<td><a href="restaurants/' + str(RestRec.id) + '/edit">Edit</a></td>'
        restaurant_list += '<td><a href="restaurants/' + str(RestRec.id) + '/delete">Delete</a></td>'
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
    new_page += "<h2>Make A New Restaurant</h2>"
    new_page += "<p></p>"
    new_page += '''<form method='POST' name='newr_post' enctype='multipart/form-data' action='newr_post'> \
                      <input name='message' type='text'> \
                      <input type='submit' vatue='Create'> \ 
                      <input id='label' name='label' type='hidden' value='newr_post'> \
                   </form>'''
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
    hello_page += '''<form method='POST' name='hello' enctype='multipart/form-data'  \
                      action='hello'><h2>What would you like me to say?</h2> \
                         <input name='message' type='text'> \
                         <input type='submit' vatue='Submit'> \
                         <input id='label' name='label' type='hidden' value='hello'> \
                     </form>'''
    hello_page += "</body></html>"
    return hello_page

##---------------------------------------------------------------------------##
##  New Restaurant Post Type -- send back results db update
##---------------------------------------------------------------------------##  
def newr_post_type(My_messagecontent, My_Form_Label):      
    # Rebuild / Sending Restaurant Name Page
    Get_File_Content = restaurants_htm()
    
    print My_Form_Label + " form processed. Returning new list."
    return Get_File_Content
            
##---------------------------------------------------------------------------##
##  Hello Post Type -- send back desired message
##---------------------------------------------------------------------------##  
def hello_post_type(My_messagecontent, My_Form_Label):        
    # Hello post of what to say    
    output = ""
    output += "<html>"
    output += '''<head><link rel="icon" href="data:,"></head>'''
    output += "<body>"
    output += "<h2>OK, how about this: </h2>"
    output += "<h1> %s </h1>" % str(My_messagecontent)
    output += "<p></p>"
    output += '''<form method='POST' name='hello' enctype='multipart/form-data'  \
                  action='hello'><h2>What would you like me to say?</h2> \
                    <input name='message' type='text'> \
                    <input type='submit' value='Submit'> \
                    <input id='label' name='label' type='hidden' value='hello'> \
                 </form>'''
    output += "</body></html>"
   
    print My_Form_Label + " form processed. Returning " + str(My_messagecontent)
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Unrecognized Resource Request
##---------------------------------------------------------------------------##  
def unrec_get(My_getfile):
    # No Idea What Requested    
    output = ""
    output += "<html>"
    output += '''<head><link rel="icon" href="data:,"></head>'''
    output += "<body>"
    output += "<h2>Error: Could not find requested resource.</h2>"
    output += "<p></p>"
    output += "Resource:    " + "\t" + My_getfile
    output += "<p></p>"
    output += "</body></html>"
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Unrecognized Post Type
##---------------------------------------------------------------------------##  
def unrec_post_type(My_ctype, My_messagecontent, My_Form_Label):
    # No Idea What Posted    
    output = ""
    output += "<html>"
    output += '''<head><link rel="icon" href="data:,"></head>'''
    output += "<body>"
    output += "<h2>Error: Unrecognized Post Request Type</h2>"
    output += "<p></p>"
    output += "Format:    " + "\t" + My_ctype + " <br>"
    output += "Message:   " + "\t" + My_messagecontent + " <br>"
    output += "Post Type: " + "\t" + My_Form_Label + " <br>"  
    output += "<p></p>"
    output += "</body></html>"
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Invalid Post Format Type
##---------------------------------------------------------------------------##  
def ifmt_post_type(My_ctype, My_messagecontent, My_Form_Label):
    # No Idea What Posted    
    output = ""
    output += "<html>"
    output += '''<head><link rel="icon" href="data:,"></head>'''
    output += "<body>"
    output += "<h2>Error: Invalid Post Format Type</h2>"
    output += "<p></p>"
    output += "Format:    " + "\t" + My_ctype + " <br>"
    output += "Message:   " + "\t" + My_messagecontent + " <br>"
    output += "Post Type: " + "\t" + My_Form_Label + " <br>" 
    output += "<p></p>"
    output += "</body></html>"
    return output


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
