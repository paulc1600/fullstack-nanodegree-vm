from flask import Flask
from urllib2 import urlopen

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    hello_page = ""
    hello_page += "<html>\n"
    hello_page += '''<head><link rel="icon" href="data:,"></head>\n'''
    hello_page += "<body>Hello World!\n"
    hello_page += "<p></p>\n"
    hello_page += "</body></html>\n"
    return "Hello World"

if __name__ == '__main__':
    My_IP = urlopen('http://ip.42.pl/raw').read()
    print My_IP
    app.debug = True
    app.run(host=My_IP, port=5000)
