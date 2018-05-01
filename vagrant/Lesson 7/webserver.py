# encoding=utf8

import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

message = ""

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        My_Path = os.getcwd()     # returns a string representing the current working directory
        Req_File = str(self.path)
        
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
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
            else:  # URL contains no valid path message
                os.chdir(My_Path)
                Get_File = Req_File.replace("/", "")
                try:
                    filep = open(Get_File, "r")
                    file.close()
                    message = ""
                    message = read_file(Get_File)
                    self.wfile.write(message)
                    print Get_File + " file sent"
                    return                        
                except IOError:
                    error1 = "Could not read " + Get_File
                    self.send_error(404, error1)

 
def read_file(filename):
    file = open(filename, "r") 
    my_message = file.read() 
    file.close()
    return my_message


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
