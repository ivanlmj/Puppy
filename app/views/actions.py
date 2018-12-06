

from json import dumps
import requests
from app import (
    app,
    abort,
    render_template,
    redirect,
    render_template,
    request
)
from app.modules import actions


@app.route("/panel/actions", methods = ['GET'])
def f_actions():
    if request.method == "GET":
        if "logged_in" in session:
            action = actions.Action()
            list_actions = action.show()
            return dumps(list_actions)
        abort(401) # Not Authorized (must authenticate)
    else:
        abort(405) # Method Not Allowed


@app.route("/panel/actions/create", methods = ['GET'])
def f_actions_create():
    if request.method == "GET":
        if "logged_in" in session:
            return render_template("action_form.html")
        return redirect("/login")
    else:
        abort(405) # Method Not Allowed


@app.route("/panel/actions/update/<int:id>", methods = ['GET'])
def f_actions_update(action_id):
    if request.method == "GET":
        if "logged_in" in session:
            api_uri = "http://127.0.0.1:5000/api/v1.0/actions" + "/" + action_id
            update_action = actions.Action()
            r  = requests.get(api_uri)
            return render_template("action_form.html", action_data = r.text)
        return redirect("/login")
    else:
        abort(405) # Method Not Allowed


@app.route("/panel/actions/run/<int:action_id>", methods = ['GET'])
def f_actions_run(action_id):
    if request.method == "GET":
        if "logged_in" in session:
            username = request.cookies.get("username")
            action = actions.Action()
            result = action.run(action_id, username)
            return str(result)
        return redirect("/login")
    else:
        abort(405) # Method Not Allowed
