from flask import Flask
import socket
import os

def get_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        massage = f"Greetings !!!\nThis is your server answering from pod:\n"
        host_name_massage = "Host Name:" + host_name
        host_ip_massage = "IP Address:" + host_ip
        content = massage+ host_name_massage + host_ip_massage
        return content

    return app

def get_host_name():
    return socket.gethostname()

def get_host_ip():
    host_name = socket.gethostname()
    return socket.gethostbyname(host_name)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app = get_app()
    app.run(debug=True, host='0.0.0.0', port=port)
