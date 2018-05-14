from flask import Flask
from urllib2 import urlopen

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    My_IP = urlopen('http://ip.42.pl/raw').read()
    print My_IP
    app.debug = True
    app.run(host=My_IP, port=5000)
