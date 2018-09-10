#!/usr/bin/python3


from flask import Flask, redirect, render_template, request
from json import dumps

from modules import actions
from modules import users

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
        user = users.User()
        status = user.login(username, password)
        if status == 0:
            return redirect("/panel")
        else:
            print("Status:", status)
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
    if request.method == "POST":
        action_id = request.form["action_id"]
        username = request.cookies.get('username')
        action = actions.Action()
        result = action.run(action_id, username)
        if result == 0:
            return "Command OK!"
        else:
            return "Command not worked..."


@app.route("/panel/actions", methods=['GET'])
def f_actions():
    action = actions.Action()
    load_actions = action.show()
    return dumps(load_actions)


@app.route("/panel/actions/logged", methods=['GET'])
def f_logged_actions():
    action = actions.Action()
    logged = action.logged()
    return dumps(logged)



if __name__ == "__main__":
    app.run(debug=True)
