#!/usr/bin/python3


from flask import Flask, redirect, render_template, request
from json import dumps
from modules.database import SQLite

__author__ = "@ivanleoncz"

app = Flask(__name__)

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
        db = SQLite()
        status = db.login(username, password)
        if status == 0:
            return redirect("/panel")
        else:
            message = "Check Username and Password."
            return render_template("login.html", login_status=message)


@app.route("/panel", methods=['GET'])
def f_panel():
    return render_template("panel.html")


@app.route("/panel/edit", methods=['GET'])
def f_panel_edit():
    return render_template("panel_edit.html")


@app.route("/panel/run", methods=['POST'])
def f_panel_run():
    if request.method = "POST":
        db = SQLite()
        action_id = request.form["action_id"]
        result = db.run_action(action_id)
        if result == 0:
            return "Command OK!"
        else
            return "Command not worked..."


@app.route("/actions", methods=['GET', 'POST'])
@app.route("/actions/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def f_actions(id=None):
    db = SQLite()
    if id is None:
        if request.method == "GET":
            actions = db.actions()
            return dumps(actions)
        elif request.method == "POST":
            name = request.form["name"]
            action = request.form["action"]
            db.create_action(name, action)
    else:
        if request.method == "GET":
            action = db.actions()
            return dumps(actions)
        elif request.method == "PUT":
        elif request.method == "DELETE":



@app.route("/logged_actions", methods=['GET'])
def f_logged_actions():
    db = SQLite()
    logged_actions = db.logged_actions()
    return dumps(logged_actions)


if __name__ == "__main__":
    app.run(debug=True)
