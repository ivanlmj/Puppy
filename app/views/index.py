""" Module for '/' route """

from app import app, abort, render_template, request


@app.route("/", methods = ['GET'])
@app.route("/index", methods = ['GET'])
def f_index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return abort(405)
