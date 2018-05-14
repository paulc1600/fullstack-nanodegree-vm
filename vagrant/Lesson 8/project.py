from flask import Flask
import socket

app = Flask(__name__)
My_IP = socket.gethostbyname(socket.gethostname())
print My_IP

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
