from flask import Flask, request
import socket  

def get_app ():
    app=Flask(__name__)
    
    @app.router('/')
    def home():
        host_name = get_host_name
        host_ip =  get_host_ip
        content = f"Greetings !!!\n ""This is your server answering from pod:\n""Host Name: {host_name}\nIP Address: {host_ip}"
        return content
        


def get_host_name ():   
    hostname=socket.gethostname()
    return hostname

def get_host_ip ():    
    IPAddr=socket.gethostbyname(hostname)
    return IPAddr


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)