import os
from flask import Flask, redirect
import socket
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/<address>/<port>')
def connect(address, port):
    ip = socket.gethostbyname(address)
    return redirect(f"steam://connect/{ip}:{port}")

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv("HOST"), port=os.getenv("PORT"))