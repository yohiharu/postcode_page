#!/usr/bin/python3

from flask import Flask
from flask import render_template, request
import api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/form")
def form():
    code = request.args["code"]
    address = api.get_address(code)
    if address == "error":
        return render_template(
            "error.html"
        )
    else:
        return render_template(
            "result.html",
            address = address
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443)
