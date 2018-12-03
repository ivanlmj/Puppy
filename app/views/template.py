
from app import app, render_template

@app.route("/template", methods=['GET'])
def f_template():
    return render_template("template.html")

