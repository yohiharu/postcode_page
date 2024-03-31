#!/usr/bin/python3

from flask import Flask
from flask import render_template, request, redirect
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
        con.execute("INSERT INTO codes(code) VALUES(?)", [int(code)])
        con.commit()
        con.close()
        return render_template(
            "result.html",
            address = address
        )

@app.route("/history")
def history():
    con = sqlite3.connect(DATABASE)
    codes = con.execute("SELECT id, code from codes").fetchall()
    codes.reverse()
    return render_template("history.html",
        codes=codes
    )

@app.route("/del/<int:id>")
def dele(id):
    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM codes where id = {}".format(id))
    con.commit()
    con.close()
    return redirect("/history")

if __name__ == "__main__":
    db.create_table(DATABASE)
    app.run(host="0.0.0.0", port=443)
