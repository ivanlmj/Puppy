

from json import dumps
from app import app, render_template, redirect, render_template, request
from app.modules import actions
from app.modules import users

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
