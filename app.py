#!/usr/bin/python3


from flask import Flask, redirect, render_template, request
from json import dumps
from modules.database import SQLite

__author__ = "@ivanleoncz"

app = Flask(__name__)
db = SQLite()

@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def f_index():
    return redirect("/login")


@app.route("/login", methods=['GET', 'POST'])
def f_login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        status = db.login(username, password)
        if status == 0:
            return redirect("/panel")
        else:
            message = "Check Username and Password."
            return render_template("login.html", login_status=message)


@app.route("/panel", methods=['GET', 'POST'])
def f_panel():
    if request.method == 'GET':
        return render_template("panel.html")
    elif request.method == 'POST':
        if request.form["operation"] == "block_site":
            return "Blocked!"
        else:
            return "Operation Not Recognized..."


@app.route("/actions", methods=['GET'])
def f_actions():
    actions = db.list_actions()
    return dumps(actions)


if __name__ == "__main__":
    app.run()
