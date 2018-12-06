""" REST-like API for CRUD operations. """

from json import dumps
from app import app, abort, request
from app.modules import actions

API_VERBS = ["POST", "GET", "PUT, DELETE"]


@app.route("/api/v1.0/actions")
@app.route("/api/v1.0/actions/<int:action_id>", methods = API_VERBS)
def f_actions(action_id=None):
    if request.method == "POST":
        # Create
        name = request.form.get("name")
        command = request.form.get("command")
        new_action = actions.Action()
        result = new_action.create(name, command)
        return str(result)
    elif request.method == "GET":
        # Read
        if action_id is None:
            created_actions =  actions.Action()
            result = created_actions.show()
            return str(result)
        else:
            created_action = actions.Action()
            result = created_action.show(action_id)
            return str(result)
    elif request.method == "PUT":
        # Update
        if actions_id is not None:
            name = request.form.get("name")
            command = request.form.get("command")
            update_action = actions.Actions()
            result = update_action.update(action_id, name, command)
            return str(result)
        else:
            abort(400) # Bad Request
    elif request.method == "DELETE":
        # Delete
        if action_id is not None:
            delete_action = actions.Actions()
            result = delete_action.delete(action_id)
            return str(result)
        else:
            abort(400) # Bad Request
    else:
        abort(405) # Method Not Allowed


@app.route("/api/v1.0/actions/history", methods = ["GET"])
def f_history():
    if request.method == "GET":
        action = actions.Action()
        history = action.history()
        return dumps(history)
    else:
        abort(405)
