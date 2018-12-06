""" Module for '/' and '/index' routes. """

from app import app, abort, redirect, request, session


@app.route("/", methods = ['GET'])
@app.route("/index", methods = ['GET'])
def f_index():
    if request.method == "GET":
        if "logged_in" in session:
            return redirect("/panel")
        return redirect("/login")
    else:
        return abort(405)
