import json
from flask import Flask, request

from function import generate_qrcode_main

app = Flask(__name__)


@app.route("/generate_qrcode", methods=["POST"])
def hello_world():
    generate_qrcode_main(json.loads(request.data))
    return "<p>Hello, World!</p>"
