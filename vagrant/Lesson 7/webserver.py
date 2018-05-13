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
Rest_List = []

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
 
            if ('restaurants' in Get_File) or Get_File == 'index':
                lupath = len(Get_File)
                if (lupath <= 11):  
                    Get_File_Content = restaurants_htm()
                    Cache_File = 'restaurants.htm'
                else:
                    Get_File = str(self.path)
                    lupath = len(Get_File)
                    Get_File = Get_File[1:lupath]
                    lupath = len(Get_File)
                    
                    nfs = Get_File[12:lupath].find('/')
                    R_id = Get_File[12:nfs+12]
                    R_fnc = Get_File[nfs+13:lupath]
                    
                    s_R_fnc = str(R_fnc)
                    
                    print "Get_File = " + Get_File
                    print "nfs = " + str(nfs)
                    print "R_id = " + R_id
                    print "R_fnc = " + R_fnc
                    
                    if s_R_fnc == 'edit':
                        Get_File_Content = rest_edit_htm(R_id)
                        Cache_File = 'restaurants_edit.htm'
                    else:
                        if s_R_fnc == 'delete':
                            Get_File_Content = rest_delete_htm(R_id)
                            Cache_File = 'restaurants_delete.htm'
                        else:
                            Get_File_Content = unrec_get(Get_File)
                            Cache_File = 'restaurants_unrec.htm'
            else:
                if Get_File == 'rest_new':
                    Get_File_Content = rest_new_htm()
                    Cache_File = 'rest_new.htm'
                else:
                    if Get_File == 'hello':
                        Get_File_Content = hello_htm()
                        Cache_File = 'hello.htm'
                    else:
                        Get_File_Content = unrec_get(Get_File)
                        Cache_File = 'cache/' + Get_File + '.htm'
                    
            # Send message first
            self.wfile.write(Get_File_Content)
            print Get_File_Content
            
            # Create Cache Copy / Debug, etc. 
            Cache_Path = os.path.join(os.getcwd(), 'cache')
            if not os.path.exists(Cache_Path):
                os.makedirs(Cache_Path)
            
            Cache_Location = os.path.join(Cache_Path, Cache_File)
            write_file(Cache_Location, Get_File_Content)
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
            Post_File = str(self.path)
            pflen = len(Post_File)
            # Post_File = Post_File[1:pflen]
            # pflen = len(Post_File)            
            
            if ('restaurants' in Post_File):
                nfs = Post_File[11:pflen].find('/')
                R_id = Post_File[11:nfs+11]
                R_fnc = Post_File[nfs+12:pflen]
                
                lu_id = int(R_id)
                s_R_fnc = str(R_fnc)

                print "Post_File = " + Post_File
                print "nfs = " + str(nfs)
                print "R_id = " + R_id
                print "R_fnc = " + R_fnc

                if s_R_fnc == 'edit':
                    NewRestName = session.query(Restaurant).filter_by(id=lu_id).one()
                    NewRestName.name = messagecontent
                    session.add(NewRestName)
                    session.commit() 

                    output_msg = restaurants_htm()
                    self.wfile.write(output_msg)
                    return
                else:
                    if s_R_fnc == 'delete':
                        output_msg = post_delete_htm(R_id)
                        self.wfile.write(output_msg)
                        return
                    else:
                        print 'Not edit or del = ' + s_R_fnc    
                        output_msg = unrec_post_type(ctype, messagecontent, s_R_fnc)
                        self.wfile.write(output_msg)
                        return
                
            else:
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
        one_rest = [RestRec.id, str(RestRec.name)]
        Rest_List.append(one_rest)
    Final_HTML = restaurants_page.format(rest_list=restaurant_list)    
    return Final_HTML


##---------------------------------------------------------------------------##
##  Create HTML for new restaurant code
##---------------------------------------------------------------------------##
def rest_new_htm():
    new_page = ""
    new_page += "<html>\n"
    new_page += '''<head><link rel="icon" href="data:,"></head>\n'''
    new_page += "<body>\n"
    new_page += "<h2>Make A New Restaurant</h2>\n"
    new_page += "<p></p>\n"
    new_page += '''<form method='POST' name='newr_post' enctype='multipart/form-data' action='newr_post'>\n \
                      <input name='message' type='text'>\n \
                      <input type='submit' vatue='Create'>\n \ 
                      <input id='label' name='label' type='hidden' value='newr_post'>\n \
                   </form>\n'''
    new_page += "</body>\n"
    new_page += "</html>\n"
    return new_page


##---------------------------------------------------------------------------##
##  Create HTML to edit restaurant name
##---------------------------------------------------------------------------##
def rest_edit_htm(My_id):
    old_rest_name = 'Unknown'
    for one_rest in Rest_List:
        one_id = one_rest[0]
        one_name = one_rest[1]
        lu_id = int(one_id)
        print "one_id = " + str(one_id)
        print "one_name = " + str(one_name)
        if lu_id == My_id:
            old_rest_name = one_name     
    
    Post_Path = 'restaurants/' + str(My_id) + '/edit'
    
    edit_page = ""
    edit_page += "<html>\n"
    edit_page += '''<head><link rel="icon" href="data:,"></head>\n'''
    edit_page += "<body>\n"
    edit_page += "<h2>Edit Restaurant Information</h2>\n"
    edit_page += "<p></p>\n"
    edit_page += '''<form method='POST' name='edit' enctype='multipart/form-data' action='{action_name}'>\n \
                      <label for="message">{old_name}</label>\n \
                      <input name='message' type='text'>\n \
                      <input type='submit' value='Rename'>\n \ 
                      <input id='label' name='label' type='hidden' value='{value_name}'>\n \
                   </form>\n'''
    edit_page += "</body>\n"
    edit_page += "</html>\n"
    Final_HTML = edit_page.format(action_name=Post_Path, old_name=old_rest_name, value_name=Post_Path)
    return Final_HTML
    
##---------------------------------------------------------------------------##
##  Create HTML to delete restaurant
##---------------------------------------------------------------------------##
## def rest_delete_htm(My_id):

    
##---------------------------------------------------------------------------##
##  Create HTML for hello code
##---------------------------------------------------------------------------##
def hello_htm():
    hello_page = ""
    hello_page += "<html>\n"
    hello_page += '''<head><link rel="icon" href="data:,"></head>\n'''
    hello_page += "<body>Hello!\n"
    hello_page += "<p></p>\n"
    hello_page += '''<form method='POST' name='hello' enctype='multipart/form-data'  \
                      action='hello'>\n<h2>What would you like me to say?</h2>\n \
                         <input name='message' type='text'>\n \
                         <input type='submit' vatue='Submit'>\n \
                         <input id='label' name='label' type='hidden' value='hello'>\n \
                     </form>'''
    hello_page += "</body></html>\n"
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
    output += "<html>\n"
    output += '''<head><link rel="icon" href="data:,"></head>\n'''
    output += "<body>\n"
    output += "<h2>OK, how about this: </h2>\n"
    output += "<h1> %s </h1>\n" % str(My_messagecontent)
    output += "<p></p>\n"
    output += '''<form method='POST' name='hello' enctype='multipart/form-data'  \
                  action='hello'>\n<h2>What would you like me to say?</h2>\n \
                    <input name='message' type='text'>\n \
                    <input type='submit' value='Submit'>\n \
                    <input id='label' name='label' type='hidden' value='hello'>\n \
                 </form>\n'''
    output += "</body></html>\n"
   
    print My_Form_Label + " form processed. Returning " + str(My_messagecontent)
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Unrecognized Resource Request
##---------------------------------------------------------------------------##  
def unrec_get(My_getfile):
    # No Idea What Requested    
    output = ""
    output += "<html>\n"
    output += '''<head><link rel="icon" href="data:,"></head>\n'''
    output += "<body>\n"
    output += "<h2>Error: Could not find requested resource.</h2>\n"
    output += "<p></p>\n"
    output += "Resource:    " + "\t" + My_getfile + "\n"
    output += "<p></p>\n"
    output += "</body></html>\n"
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Unrecognized Post Type
##---------------------------------------------------------------------------##  
def unrec_post_type(My_ctype, My_messagecontent, My_Form_Label):
    # No Idea What Posted    
    output = ""
    output += "<html>\n"
    output += '''<head><link rel="icon" href="data:,"></head>\n'''
    output += "<body>\n"
    output += "<h2>Error: Unrecognized Post Request Type</h2>\n"
    output += "<p></p>\n"
    output += "Format:    " + "\t" + My_ctype + " <br>\n"
    output += "Message:   " + "\t" + My_messagecontent + " <br>\n"
    output += "Post Type: " + "\t" + My_Form_Label + " <br>\n"  
    output += "<p></p>\n"
    output += "</body></html>\n"
    return output


##---------------------------------------------------------------------------##
##  Send Back Error -- Invalid Post Format Type
##---------------------------------------------------------------------------##  
def ifmt_post_type(My_ctype, My_messagecontent, My_Form_Label):
    # No Idea What Posted    
    output = ""
    output += "<html>\n"
    output += '''<head><link rel="icon" href="data:,"></head>\n'''
    output += "<body>\n"
    output += "<h2>Error: Invalid Post Format Type</h2>\n"
    output += "<p></p>\n"
    output += "Format:    " + "\t" + My_ctype + " <br>\n"
    output += "Message:   " + "\t" + My_messagecontent + " <br>\n"
    output += "Post Type: " + "\t" + My_Form_Label + " <br>\n" 
    output += "<p></p>\n"
    output += "</body></html>\n"
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
