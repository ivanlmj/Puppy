#!/usr/bin/python3


from flask import Flask, make_response, redirect, render_template, request
from json import dumps

from modules import actions
from modules import users

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/template", methods=['GET'])
def f_template():
    return render_template("template.html")


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
            response = make_response(redirect('/panel'))
            response.set_cookie('username', username)
            return response
        else:
            print("Status:", status)
            message = "Check Username and Password."
            return render_template("login.html", login_status=message)


@app.route("/panel", methods=['GET'])
def f_panel():
    return render_template("panel.html")


@app.route("/panel/action", methods=['GET'])
def f_action():
    if request.method == "GET":
        return render_template("action.html")


@app.route("/panel/action/<option>", methods=['POST'])
def f_panel_action(option):
    if request.method == "POST":
        response = make_response(redirect('/panel'))
        action_obj = actions.Action()
        if option == "run":
            action_id = request.form["action_id"]
            username = request.cookies.get('username')
            result = action_obj.run(action_id, username)
            response.set_cookie('run_status', str(result))
        elif option == "create":
            name = request.form["name"]
            action = request.form["action"]
            result = action_obj.create(name, action)
            response.set_cookie('create_status', str(result))
        elif option == "update":
            action_id = request.form["id"]
            name = request.form["name"]
            action = request.form["action"]
            result = action_obj.update(action_id, name, action)
            response.set_cookie('update_status', str(result))
        elif option == "delete":
            action_id = request.form["id"]
            result = action_obj.delete(action_id)
            response.set_cookie('delete_status', str(result))

        return response


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
