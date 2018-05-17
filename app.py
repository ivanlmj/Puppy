#!/usr/bin/python3


from flask import Flask, redirect, render_template, request

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
        return redirect("/panel")


@app.route("/panel", methods=['GET', 'POST'])
def f_panel():
    if request.method == 'GET':
        return render_template("panel.html")
    elif request.method == 'POST':
        if request.form["operation"] == "block_site":
            return "Blocked!"
        else:
            return "Operation Not Recognized..."


if __name__ == "__main__":
    app.run()
