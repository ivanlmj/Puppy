
from app import app, redirect

@app.route("/", methods=['GET'])                                                
@app.route("/index", methods=['GET'])                                           
def f_index():                                                                  
    return redirect("/login")
