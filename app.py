import json
from flask import Flask, request

from function import generate_qrcode_main
from utils import REQUIRED_VARIABLE

app = Flask(__name__)


@app.route("/generate_qrcode", methods=["POST"])
def hello_world():
    data = json.loads(request.data)
    if set(REQUIRED_VARIABLE).issubset(data):
        return generate_qrcode_main(data)
    else:
        required_variable = ", ".join([str(elem) for elem in REQUIRED_VARIABLE])
        return {
            "status": False,
            "msg": f"You need to pass all required parameters({required_variable})",
        }
