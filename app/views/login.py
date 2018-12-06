
""" Module for /login route. """

from app import (
        app,
        abort,
        make_response,
        redirect,
        render_template,
        request,
        session
)

from app.modules import users


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
            session["logged_in"] = True
            response = make_response(redirect('/panel'))
            response.set_cookie('username', username)
            return response
        else:
            print("Status:", status)
            message = "Check Username and Password."
            return render_template("login.html", login_status=message)
    else:
        abort(405)

