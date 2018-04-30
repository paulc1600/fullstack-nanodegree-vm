# encoding=utf8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

message = ""

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
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
                read_file("easyftp.htm")
                self.wfile.write(message)
                print "easyftp.htm file sent"
                return
            else:  # URL contains no valid path message
                self.send_error(404, 'File Not Found: %s' % self.path)

 
def read_file(filename):
    file = open(filename, "r") 
    message = file.read() 
    file.close()
    return


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
