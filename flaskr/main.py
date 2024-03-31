#!/usr/bin/python3

from flask import Flask
from flask import render_template, request
import sqlite3

import api
import db

DATABASE = "database.db"

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
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO codes VALUES(?)", [int(code)])
        con.commit()
        con.close()
        return render_template(
            "result.html",
            address = address
        )

@app.route("/history")
def history():
    con = sqlite3.connect(DATABASE)
    codes = con.execute("SELECT code from codes").fetchall()
    codes = [i[0] for i in codes]
    codes.reverse()
    return render_template("history.html",
        codes=codes
    )
if __name__ == "__main__":
    db.create_table(DATABASE)
    app.run(host="0.0.0.0", port=443)
