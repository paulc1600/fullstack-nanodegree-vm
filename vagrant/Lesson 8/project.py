from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    My_IP = s.getsockname()[0]
    s.close()
    print My_IP
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
