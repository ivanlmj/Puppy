
from app import app, abort, redirect, render_template, request, session

@app.route("/panel", methods = ["GET"])
def f_panel():
    if request.method == "GET":
        if "logged_in" in session:
            return render_template("panel.html")
        return redirect("/login")
    else:
        abort(405)
